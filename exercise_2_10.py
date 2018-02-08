"""Output the response times (in ms, e.g., 453 for 453 ms) and accuracy 
(1 for correct, 0 for incorrect) to a file output.txt. Output one line per 
trial: each line should contain the accuracy (1 or 0) and the response time 
(in milliseconds)"""

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

trialNums = []
trialTimes = []
trialScores = []

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
    trialNum += 1 #increment trialNum to 1 right away
    startTime = core.getTime() #start timer
    
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
    
    trialTime = endTime - startTime
    if trialTime < 1:
        trialTime = str(trialTime)[2:5]
    else:
        trialTime = "1" + str(trialTime)[2:5]
    
    trialNums.append(trialNum)
    trialTimes.append(trialTime)
    trialScores.append(trialScore)
    
    trialLen = "Trial_Num" + str(trialNum) + " " + str(trialTime) + " seconds"
    print trialLen
    
    fixCross.draw()
    win.flip()
    core.wait(.5) 
    
with open('output.txt', "w") as f:
    for i in range(len(trialNums)):
        f.write(str(trialNums[i]) + "\t" + str(trialScores[i]) 
        + "\t" + str(trialTimes[i]) + "\n") 
