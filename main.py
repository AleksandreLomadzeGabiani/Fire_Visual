# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 21:36:18 2019

@author: A_Normal_PC
"""

from graphics import *
from classes import *
import time

win= GraphWin("yeet",500,500)

F=Fire((250,250),win)

while True:
    F.next_tick()
    time.sleep(1/15)

win.getMouse()

win.close()