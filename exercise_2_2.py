# Open names.txt to see what the names list looks like. Make the script show 
# last names instead of first names (don't change the names.txt file).

import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
lastNames = [name.split(' ')[1] for name in names]

win = visual.Window([800,600],color="black", units='pix')
fixCross = visual.TextStim(win, text="+", height=40, color="white",pos=[0,0])
lastNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
while True:
    fixCross.draw()
    win.flip()
    core.wait(.5)
    nameShown = random.choice(lastNames)
    lastNameStim.setText(nameShown)
    lastNameStim.draw()
    win.flip()
    core.wait(.75)
    fixCross.draw()
    win.flip()
    core.wait(.5)

    if event.getKeys(['q']):
        break