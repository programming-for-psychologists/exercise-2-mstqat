""" Create a fixation cross using a TextStim object visual.TextStim set text 
to"+" and color to "white". Make the fixation cross appear for 500 ms before 
each name and disappear right before the name comes up. """

import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]

"""
the two line above are a more compact way of writing: 
names = open('names.txt', 'r').readlines()
firstNames=[]
for name in names:
    firstNames.append(name.split(' ')[0])
"""	
win = visual.Window([800,600],color="black", units='pix')
fixCross = visual.TextStim(win, text="+", height=40, color="white",pos=[0,0])
firstNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
while True:
    fixCross.draw()
    win.flip()
    core.wait(.5)
    nameShown = random.choice(firstNames)
    firstNameStim.setText(nameShown)
    firstNameStim.draw()
    win.flip()
    core.wait(.75)
    fixCross.draw()
    win.flip()
    core.wait(.5)

    if event.getKeys(['q']):
        break