# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 21:36:18 2019

@author: A_Normal_PC
"""

from graphics import *
from classes import *
import time

win= GraphWin("fire",500,500, autoflush=False)
win.setBackground("black")

Frame_rate=30

F=Fire((250,250),win)

moving_to=None

while True:
    F.next_tick()
    last_clicked=win.checkMouse()
    
    if moving_to!=None or last_clicked!=None:
        if last_clicked!=None:
            moving_to=last_clicked
        
        current_pos=F.get_loc()
        F.set_loc((current_pos[0]-(current_pos[0]-moving_to.getX())/(Frame_rate/5),current_pos[1]-(current_pos[1]-moving_to.getY())/(Frame_rate/5)))
        
    update(Frame_rate)
    #time.sleep(1/30)
    
win.getMouse()

win.close()