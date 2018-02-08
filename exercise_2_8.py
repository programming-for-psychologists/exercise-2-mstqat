"""Extend the task by requiring the subject to respond by pressing a spacebar 
(the key is called 'space'), as quickly as possible anytime the name on the 
screen matches the name you entered into the box (so if I enter 'Gary' I would 
have to press 'space' anytime the name 'Gary' shows up. If the participant 
presses 'space' to the wrong name (false alarm), or misses the name (a miss), 
show a red X."""

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

userVar = {"Name":"Enter your first name"}
dlg = gui.DlgFromDict(userVar)


#check user name
if not userVar["Name"] in firstNames:
    errorDlg = gui.Dlg()
    errorDlg.addText("Name does not exist")
    errorDlg.show()

#display names; get user input; give feedback
while True:
    fixCross.draw()
    win.flip()
    core.wait(.5)
    nameShown = random.choice(firstNames + lastNames) # choose from mixed names
    nameStim.setText(nameShown)
    nameStim.draw()
    win.flip()
    
    if nameShown == userVar["Name"]:
        key = event.waitKeys(maxWait = 1) #no keylist arg needed
        if key == ["space"]:
            corrRes.draw()
            win.flip()
            core.wait(.5)
        else:
            wrongRes.draw()
            win.flip()
            core.wait(.5) 
    
    elif nameShown in firstNames:
        key = event.waitKeys(keyList = ["f","l","space"], maxWait = 1)
        if key == ["f"]:
            corrRes.draw()
            win.flip()
            core.wait(.5)
        elif key in [["l"],["space"],None]:
            wrongRes.draw()
            win.flip()
            core.wait(.5)    
    
    elif nameShown in lastNames:
        key = event.waitKeys(keyList = ["f","l","space"], maxWait = 1)
        if key == ["l"]:
            corrRes.draw()
            win.flip()
            core.wait(.5)
        elif key in [["f"],["space"],None]:
            wrongRes.draw()
            win.flip()
            core.wait(.5)
    
    fixCross.draw()
    win.flip()
    core.wait(.5) 