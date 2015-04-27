# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:55:15 2015

@author: Maxime
"""

k_up_is_up = False
 
while True:
    ev = event.wait()
    if ev.type == QUIT: exit()
    elif ev.type == KEYDOWN:
        if not ev.key or ev.key== K_DOWN: print 'down'
        elif ev.key == K_LEFT: print 'left'
        elif ev.key == K_RIGHT: print 'right'
        elif ev.key == K_UP and not k_up_is_up:
            print 'up'
            k_up_is_up = True
    elif ev.type == KEYUP and ev.key == K_UP: k_up_is_up = False