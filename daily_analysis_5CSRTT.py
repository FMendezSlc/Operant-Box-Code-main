import pandas as pd
import os as os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
root.call('wm', 'attributes', '.', '-topmost', True)
folder_path = filedialog.askdirectory(title="Select a folder")
root.destroy()

os.chdir(folder_path)

session_files = [file for file in os.listdir() if '.csv' in file]
training_day = os.path.dirname(folder_path)
cohort_dir = os.path.dirname(training_day)

passing_criteria = {'Stage0' : [30, 45], 'Stage1': [30, 40], 'Stage2': [30, 50], 'Stage3+': [80, 50]}

sessions_dfs = [] 

for file in session_files:
    # read each file created in the day, turn into df and concat them all
    wk_file = pd.read_csv(os.path.join(folder_path, file), 
                                        header = 1, index_col = None, skip_blank_lines = True)
    clean_file = wk_file[(wk_file['Sub_ID']!= ' ') & (wk_file['Sub_ID']!= 'None')]
    sessions_dfs.append(clean_file)
        
daily_agg = pd.concat(sessions_dfs, axis = 0, ignore_index = True, verify_integrity = True)
# save the concatenated files for the day
daily_agg.to_csv(os.path.join(training_day, os.path.basename(training_day))+'_aggregate.csv', index = False)

# analyzing performance
current_performance = daily_agg[['DATA_Live', 'Sub_ID', 'TASK', 'per_accuracy', 'per_omission', 'per_correct', 'num_correct']]

current_performance = current_performance.astype({'per_accuracy':'float', 'per_omission': 'float', 'per_correct': 'float', 'num_correct': 'int'})

eval_col = []

for idx, row in current_performance.iterrows():
    if 'habituation' in row['TASK']:
        eval_ = 'habiutation'
    elif 'Stage0' in row['TASK']:
        goal = passing_criteria['Stage0']
        if row['num_correct'] >= goal[0]:
            eval_ = 'passing'
        else:
            eval_ = 'repeat'
    elif 'Stage1' in row['TASK']:
        goal = passing_criteria['Stage1']
        if (row['num_correct'] >= goal[0]) & (row['per_correct'] >= goal[1]):
            eval_ = 'passing'
        else:
            eval_ = 'repeat'
    elif 'Stage2' in row['TASK']:
        goal = passing_criteria['Stage2']
        if (row['num_correct'] >= goal[0]) & (row['per_correct'] >= goal[1]):
            eval_ = 'passing'
        else:
            eval_ = 'repeat'   
    else:
        goal = passing_criteria['Stage3+']
        if (row['per_accuracy'] >= goal[0]) & (row['per_omission'] <= goal[1]):
            eval_ = 'passing'
        else:
            eval_ = 'repeat' 
    eval_col.append(eval_)

if any('progression' in file for file in os.listdir(cohort_dir)):
    #open file and append new results
    progress_file = [file for file in os.listdir(cohort_dir) if 'progression' in file][0]
    progress_df = pd.read_csv(os.path.join(cohort_dir, progress_file), index_col = None, skip_blank_lines = True)
    
    new_status = []
    
    for pair in zip(progress_df['evaluation'], eval_col):
        if (pair[0] == 'habituation') or (pair[1]== 'habituation'):
            new_status.append('repeat')
        elif (pair[0] == 'repeat') & (pair[1]== 'repeat'):
            new_status.append('repeat')
        elif (pair[0] == 'repeat') & (pair[1]== 'passing'):
            new_status.append('passing')
        elif (pair[0] == 'passing') & (pair[1]== 'repeat'):
            new_status.append('repeat')
        elif (pair[0] == 'passing') & (pair[1]== 'passing'):
            new_status.append('promote')
            
    progress_df['evaluation'] = new_status
    date = current_performance['DATA_Live'][0].split(' ')[0]
    progress_df.insert(len(progress_df.columns)-1, date, current_performance['TASK'])
    progress_df.to_csv(os.path.join(cohort_dir, 'cohort_progression.csv'), index = False)
    

else:
    # if this the first session, create a progression df and save it to the cohort dir
    progress_df = pd.DataFrame(current_performance['Sub_ID'])
    date = current_performance['DATA_Live'][0].split(' ')[0]
    progress_df[date] = current_performance['TASK']
    progress_df['evaluation'] = eval_
    progress_df.to_csv(os.path.join(cohort_dir, 'cohort_progression.csv'), index = False)
    


