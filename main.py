# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 21:36:18 2019

@author: A_Normal_PC
"""

from graphics import *
from classes import *
import time

win= GraphWin("yeet",500,500, autoflush=False)

F=Fire((250,250),win)

while True:
    F.next_tick()
    last_clicked=win.checkMouse()
    if last_clicked!=None:
        
        F.set_loc((last_clicked.getX(),last_clicked.getY()))
    update(15)
    #time.sleep(1/30)
    
win.getMouse()

win.close()