# this helps to pre assign com numbers to box instead of typing manually every time
# User can change com number according to Box order
# example self.comboBox_srport_1.setCurrentText('com36'), this says setup1 box1 com number com4.
# So by changing com4 to any com* any number, one can change box to com assignment

def select_setup_1(self):
    self.comboBox_srport_1.setCurrentText('com14')
    self.comboBox_srport_2.setCurrentText('com15')
    self.comboBox_srport_3.setCurrentText('com6')
    self.comboBox_srport_4.setCurrentText('com3')
    self.comboBox_srport_5.setCurrentText('com11')
    self.comboBox_srport_6.setCurrentText('com5')
    self.comboBox_srport_7.setCurrentText('com12')
    self.comboBox_srport_8.setCurrentText('com13')

    self.pushButton_setupselect_1.setStyleSheet('Setup_1')
    self.pushButton_setupselect_1.setText('SetUp1 : 01 - 08')
    self.pushButton_setupselect_2.setStyleSheet('Setup_2')
    self.pushButton_setupselect_3.setStyleSheet('Setup_3')
    self.pushButton_setupselect_1.setEnabled(False)
    self.pushButton_setupselect_2.setEnabled(False)
    self.pushButton_setupselect_3.setEnabled(False)
    self.pushButton_setupselect_2.setText(' ')
    self.pushButton_setupselect_3.setText(' ')
    self.label_box1.setText('Box 01')
    self.label_box2.setText('Box 02')
    self.label_box3.setText('Box 03')
    self.label_box4.setText('Box 04')
    self.label_box5.setText('Box 05')
    self.label_box6.setText('Box 06')
    self.label_box7.setText('Box 07')
    self.label_box8.setText('Box 08')

def select_setup_2(self):
    self.comboBox_srport_1.setCurrentText('com12')
    self.comboBox_srport_2.setCurrentText('com13')
    self.comboBox_srport_3.setCurrentText('com14')
    self.comboBox_srport_4.setCurrentText('com15')
    self.comboBox_srport_5.setCurrentText('com16')
    self.comboBox_srport_6.setCurrentText('com17')
    self.comboBox_srport_7.setCurrentText('com18')
    self.comboBox_srport_8.setCurrentText('com19')
    self.pushButton_setupselect_1.setStyleSheet('Setup_2')
    self.pushButton_setupselect_2.setText('SetUp2: 09 - 16')
    self.pushButton_setupselect_1.setStyleSheet('Setup_1')
    self.pushButton_setupselect_3.setStyleSheet('Setup_3')
    self.pushButton_setupselect_1.setEnabled(False)
    self.pushButton_setupselect_2.setEnabled(False)
    self.pushButton_setupselect_3.setEnabled(False)
    self.pushButton_setupselect_1.setText(' ')
    self.pushButton_setupselect_3.setText(' ')
    self.label_box1.setText('Box 09')
    self.label_box2.setText('Box 10')
    self.label_box3.setText('Box 11')
    self.label_box4.setText('Box 12')
    self.label_box5.setText('Box 13')
    self.label_box6.setText('Box 14')
    self.label_box7.setText('Box 15')
    self.label_box8.setText('Box 16')

def select_setup_3(self):
    self.comboBox_srport_1.setCurrentText('com20')
    self.comboBox_srport_2.setCurrentText('com21')
    self.comboBox_srport_3.setCurrentText('com22')
    self.comboBox_srport_4.setCurrentText('com23')
    self.comboBox_srport_5.setCurrentText('')
    self.comboBox_srport_6.setCurrentText('')
    self.comboBox_srport_7.setCurrentText('')
    self.comboBox_srport_8.setCurrentText('')
    self.pushButton_setupselect_1.setStyleSheet('Setup_3')
    self.pushButton_setupselect_3.setText('SetUp3: 17 - 24')
    self.pushButton_setupselect_1.setStyleSheet('Setup_1')
    self.pushButton_setupselect_2.setStyleSheet('Setup_2')
    self.pushButton_setupselect_1.setEnabled(False)
    self.pushButton_setupselect_2.setEnabled(False)
    self.pushButton_setupselect_3.setEnabled(False)
    self.pushButton_setupselect_1.setText(' ')
    self.pushButton_setupselect_2.setText(' ')
    self.label_box1.setText('Box 17')
    self.label_box2.setText('Box 18')
    self.label_box3.setText('Box 19')
    self.label_box4.setText('Box 20')
    self.label_box5.setText('Box 21')
    self.label_box6.setText('Box 22')
    self.label_box7.setText('Box 23')
    self.label_box8.setText('Box 24')
