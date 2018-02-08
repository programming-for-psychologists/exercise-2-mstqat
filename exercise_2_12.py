"""Bonus: You've probably noticed that the name you typed in 
only appears rarely (in fact, it will appear 1/# of people in the class, 
on average). Change the code so that the name you entered appears on 1/4 of 
the trials."""

#Do something new. Compare response times to first and last names, 
#measure effect of font face, etc.

import time
import sys
import random
from psychopy import visual,event,core,gui

#variables
names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]
lastNames = [name.split(' ')[1][:-1] for name in names] #chop off the newline
win = visual.Window([800,600],color="black", units='pix')
fixCross = visual.TextStim(win, text="+", height=40, color="white",pos=[0,0])
nameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
corrRes = visual.TextStim(win,text="O",height=40, color="green",pos=[0,0])
wrongRes = visual.TextStim(win,text="X",height=40, color="red",pos=[0,0])
trialNum = 0


userVar = {"Name":"Enter your first name"}
dlg = gui.DlgFromDict(userVar)

trialNums = []      #stores trial numbers
trialTimes = []     #stores response times
trialScores = []    #stores response accuracy, per trial
trialNames = []     #stores all names shown
trialLastName = []  #stores 1 for each last name shown

#check user name
if not userVar["Name"] in firstNames:
    errorDlg = gui.Dlg()
    errorDlg.addText("Name does not exist")
    errorDlg.show()

#display names; get user input; give feedback
for i in range(5):
    
    fixCross.draw()
    win.flip()
    core.wait(.5)
    nameShown = random.choice(firstNames + lastNames) # choose from mixed names
    nameStim.setText(nameShown)
    nameStim.draw()
    win.flip()
    trialNum += 1                #increment trialNum to 1 right away
    startTime = core.getTime()   #start timer
    firstOrLast = 0              #stores 1 if last name was shown
  
    if nameShown == userVar["Name"]:
        key = event.waitKeys(maxWait = 1) #no keylist arg needed
        endTime = core.getTime()
        if key == ["space"]:
            corrRes.draw()
            win.flip()
            core.wait(.5)
            trialScore = 1
        else:
            wrongRes.draw()
            win.flip()
            core.wait(.5)
            trialScore = 0
    
    elif nameShown in firstNames:
        key = event.waitKeys(keyList = ["f","l","space"], maxWait = 1)
        endTime = core.getTime()
        if key == ["f"]:
            corrRes.draw()
            win.flip()
            core.wait(.5)
            trialScore = 1
        elif key in [["l"],["space"],None]:
            wrongRes.draw()
            win.flip()
            core.wait(.5) 
            trialScore = 0
    
    elif nameShown in lastNames:
        key = event.waitKeys(keyList = ["f","l","space"], maxWait = 1)
        endTime = core.getTime()
        firstOrLast = 1         #changes to 1 when last name shown
        if key == ["l"]:
            corrRes.draw()
            win.flip()
            core.wait(.5)
            trialScore = 1
        elif key in [["f"],["space"],None]:
            wrongRes.draw()
            win.flip()
            core.wait(.5)
            trialScore = 0
    
    #get trial time
    trialTime = endTime - startTime
    if trialTime < 1:
        trialTime = str(trialTime)[2:5]
    else:
        trialTime = "1" + str(trialTime)[2:5]
    
    trialNums.append(trialNum)
    trialTimes.append(trialTime)
    trialScores.append(trialScore)
    trialNames.append(nameShown)
    trialLastName.append(firstOrLast)
    
    trialLen = "Trial_Num" + str(trialNum) + " " + str(trialTime) + " seconds"
    print trialLen
    
    fixCross.draw()
    win.flip()
    core.wait(.5) 
    
#output includes tab-delimited columns for each name, and whether the name was 
#a first or last name
with open('output.txt', "w") as f:
    for i in range(len(trialNums)):
        f.write(str(trialNums[i]) + "\t" + str(trialScores[i]) 
        + "\t" + str(trialTimes[i]) + "\t" + str(trialNames[i]) + "\t"
        + str(trialLastName[i]) + "\n" ) 
