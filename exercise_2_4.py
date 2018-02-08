""" On each presentation of a name, wait for a response 
('f' for first name, 'l' for last-name) and only proceed to the next name if 
the response is correct. Hint: if you've done steps 2-3 properly, this should 
be really easy. Refer to the psychopy documentation of event.waitKeys() if 
you have trouble. """

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

while True:
    fixCross.draw()
    win.flip()
    core.wait(.5)
    nameShown = random.choice(firstNames + lastNames) # choose from mixed names
    nameStim.setText(nameShown)
    nameStim.draw()
    win.flip()
    if nameShown in firstNames:
        event.waitKeys(keyList = ["f"])
    if nameShown in lastNames:
        event.waitKeys(keyList = ["l"])
    fixCross.draw()
    win.flip()
    core.wait(.5)