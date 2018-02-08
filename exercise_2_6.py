"""Now, instead of waiting for a response forever, let's implement a timeout. 
Show accuracy feedback as before, but now also show a red 'X' if no response 
is received for 1 sec (and go on to the next trial automatically following the 
feedback). (Use psychopy timers)"""

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
        key = event.waitKeys(keyList = ["f","l"], maxWait = 1)
        if key == ["f"]:
            corrRes.draw()
            win.flip()
            core.wait(.5)
        elif key in [["l"],None]:
            wrongRes.draw()
            win.flip()
            core.wait(.5)    
    if nameShown in lastNames:
        key = event.waitKeys(keyList = ["f","l"], maxWait = 1)
        if key == ["l"]:
            corrRes.draw()
            win.flip()
            core.wait(.5)
        elif key in [["f"],None]:
            wrongRes.draw()
            win.flip()
            core.wait(.5)
    fixCross.draw()
    win.flip()
    core.wait(.5)                       