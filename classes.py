# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 22:35:42 2019

@author: A_Normal_PC
"""

from graphics import *
from random import *

class Particle(object):
    
    def __init__(self,loc,accel,size,lifespan):
        """initializes a particle object in its base state"""
        self.alive=True
        self.velocity=(0,0)
        self.accel=accel
        self.loc=loc
        self.ticks_lived=0
        self.lifespan=lifespan
        self.rectangle=Rectangle(Point(loc[0]-size,loc[1]-size),Point(loc[0]+size,loc[1]+size))
        self.drawn=False
        self.rectangle.setFill("red")
    def next_tick(self,win):
        """calculates and changes state of the particle to the next tick of its existence.
         returns true if the particle is still alive and false if it is dead"""
        
        if not self.alive: #breaks executio if the particle is dead and returns false
            return self.alive
        
        if not self.drawn:
            self.draw(win)
        
        if (self.lifespan-2)==self.ticks_lived: #for the aesthetic
            self.rectangle.setFill("yellow")
            
        if (self.lifespan//2)==self.ticks_lived: #Turn around on half way point.
            self.accel=(-self.accel[0],self.accel[1])
            self.velocity=(0,self.velocity[1])
            self.rectangle.setFill("orange")
        self.velocity=(self.velocity[0]+self.accel[0],self.velocity[1]+self.accel[1])
        x,y=self.velocity
        self.rectangle.move(x,y)
        self.loc=self.rectangle.getCenter()
        self.ticks_lived=self.ticks_lived+1
        
        if self.ticks_lived==self.lifespan:
            self.die()
            return False
        else:
            return True
    
    def draw(self,window):
        """draws the visual representation of the particle to the main window"""
        self.rectangle.draw(window)
        self.drawn=True
        
    def die(self):
        """self-explanitory name."""
        self.rectangle.undraw()
        self.drawn=False
        self.alive=False
        
class Fire(object):
    
    def __init__(self,loc,win):
        """initializes a fire object"""
        self.loc=loc
        self.particles=[]
        self.win=win
    
    def set_loc(self,new_loc):
        self.loc=new_loc
        
    def spawn_particle(self):
        x_offset=randrange(-15, 15)
        y_offset=randrange(-15, 15)
        loc=(self.loc[0]+x_offset,self.loc[1]+y_offset)
        accel=(randrange(-2, 2),-randrange(1, 4))
        size=randrange(2, 3)
        lifespan=randrange(5, 10)
        return Particle(loc,accel,size,lifespan)
    
    def next_tick(self):
        for i in range(randrange(0, 30)):
            self.particles.append(self.spawn_particle())
            
        to_delete=[]
        for index in range(len(self.particles)):
            particle=self.particles[index]
            if not particle.next_tick(self.win):
                to_delete.append(index)
        
        to_delete.sort()
        num_deleted=0
        for index in to_delete:
            del self.particles[index-num_deleted]
            num_deleted+=1