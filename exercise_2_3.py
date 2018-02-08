# Make the program randomly alternate between first names and last names.

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
    core.wait(.75)
    fixCross.draw()
    win.flip()
    core.wait(.5)

    if event.getKeys(['q']):
        break