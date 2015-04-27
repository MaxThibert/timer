# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:46:16 2015

@author: Maxime
"""

def timer():
    screen = display.set_mode((200, 200))
    key.set_repeat(50, 50)
    time.set_timer(KEYDOWN, 500)
#ici l'astuce est de simuler l'appuie d'une touche
#time.set_timer() poste un evenement a interval regulier
#mais il n'est pas possible de specifier des attributs
#ainsi l'evenement KEYDOWN aura un attribut key egal a 0
#0 ne correspondant a aucune touche du clavier il n'y a pas de conflit