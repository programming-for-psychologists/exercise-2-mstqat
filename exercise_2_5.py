"""Now let's implement some feedback. Let's allow either a 'f' or 'l' response 
for each trial. If the response is correct, show a green 'O' before the start 
of the next trial. If the response is wrong, show a red 'X' (you can use 
textStim objects for feedback). Show the feedback for 500 ms. Note: we have 
someone in a class whose last name is a common first name. If this were an 
experiment, how might this affect responses?"""

import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]
lastNames = [name.split(' ')[1][:-1] for name in names] #chop off the newline

win = visual.Window([800,600],color="black", units='pix')
fixCross = visual.TextStim(win, text="+", height=40, color="white",pos=[0,0])
nameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])

corrRes = visual.TextStim(win,text="O",height=40, color="green",pos=[0,0])
wrongRes = visual.TextStim(win,text="X",height=40, color="red",pos=[0,0])

while True:
    fixCross.draw()
    win.flip()
    core.wait(.5)
    nameShown = random.choice(firstNames + lastNames) # choose from mixed names
    nameStim.setText(nameShown)
    nameStim.draw()
    win.flip()
    if nameShown in firstNames:
        key = event.waitKeys(keyList = ["f","l"])
        if key == ["f"]:
            corrRes.draw()
            win.flip()
            core.wait(.5)
        elif key == ["l"]:
            wrongRes.draw()
            win.flip()
            core.wait(.5)
    if nameShown in lastNames:
        key = event.waitKeys(keyList = ["f","l"])
        if key == ["l"]:
            corrRes.draw()
            win.flip()
            core.wait(.5)
        elif key == ["f"]:
            wrongRes.draw()
            win.flip()
            core.wait(.5)
    fixCross.draw()
    win.flip()
    core.wait(.5)