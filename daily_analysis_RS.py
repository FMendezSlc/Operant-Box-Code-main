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

passing_criteria = {'Habituation' : [30], 'Training': [30,80], 'Rule_Shift': [30,80], 'Reversal': [30,80]}

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
current_performance = daily_agg[['Date', 'BOX', 'Sub_ID', 'TASK', 'per_accuracy_unlit',
       'num_correct_lit', 'num_correct_unlit', 'per_accuracy_lit']].copy()

current_performance[current_performance == ' '] = 0.0

current_performance = current_performance.astype({'per_accuracy_lit':'float', 'num_correct_lit': 'int', 
                                                  'num_correct_unlit': 'int', 'per_accuracy_unlit':'float'})

eval_col = []

for idx, row in current_performance.iterrows():
    if 'Habituation' in row['TASK']:
        goal = passing_criteria['Habituation']
        if (row['num_correct_lit'] >= goal[0]):
            eval_ = 'passing'
        else:
            eval_ = 'repeat'
    elif 'Training' in row['TASK']:
        goal = passing_criteria['Training']
        if (row['num_correct_lit'] >= goal[0]) & (row['per_accuracy_lit'] >= goal[1]):
            eval_ = 'passing'
        else:
            eval_ = 'repeat'
    elif 'Hole2' in row['TASK']:
        goal = passing_criteria['Rule_Shift']
        if (row['num_correct_unlit'] >= goal[0]) & (row['per_accuracy_unlit'] >= goal[1]):
            eval_ = 'passing'
        else:
            eval_ = 'repeat'
    elif 'Hole4' in row['TASK']:
        goal = passing_criteria['Reversal']
        if (row['num_correct_unlit'] >= goal[0]) & (row['per_accuracy_unlit'] >= goal[1]):
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
        if (pair[0] == 'repeat') & (pair[1]== 'repeat'):
            new_status.append('repeat')
        elif (pair[0] == 'repeat') & (pair[1]== 'passing'):
            new_status.append('passing')
        elif (pair[0] == 'passing') & (pair[1]== 'repeat'):
            new_status.append('repeat')
        elif (pair[0] == 'passing') & (pair[1]== 'passing'):
            new_status.append('promote')
        elif (pair[0] == 'promote') & (pair[1]== 'repeat'):
            new_status.append('repeat')
        elif (pair[0] == 'promote') & (pair[1]== 'passing'):
            new_status.append('passing')
        elif (pair[0] == 'promote') & (pair[1]== 'promote'):
            new_status.append('passing')
        else:
            new_status.append('exception!')
            
    progress_df['evaluation'] = new_status
    date = current_performance['Date'][0].split(' ')[0]
    progress_df.insert(len(progress_df.columns)-1, date, current_performance['TASK'])
    progress_df.to_csv(os.path.join(cohort_dir, 'cohort_progression.csv'), index = False)
    

else:
    # if this the first session, create a progression df and save it to the cohort dir
    progress_df = pd.DataFrame(current_performance['Sub_ID'])
    date = current_performance['Date'][0].split(' ')[0]
    progress_df[date] = current_performance['TASK']
    progress_df['evaluation'] = eval_
    progress_df.to_csv(os.path.join(cohort_dir, 'cohort_progression.csv'), index = False)
    


