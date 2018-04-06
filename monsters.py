#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame import *

Monster1_IMG = "./img/rock1.png" 
Monster2_IMG = "./img/rock2.png" 
Monster3_IMG = "./img/rock3.png" 

class Monster_1(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        WIDTH = 94
        HEIGHT = 107
        self.image = Surface((WIDTH, HEIGHT))
        self.image = image.load("./img/monster_1.png")
        self.rect = Rect(x, y, WIDTH, HEIGHT) 

class Monster_2(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        WIDTH = 65
        HEIGHT = 89
        self.image = Surface((WIDTH, HEIGHT))
        self.image = image.load("./img/monster_2.png")
        self.rect = Rect(x, y, WIDTH, HEIGHT) 

class Monster_3(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        WIDTH = 87
        HEIGHT = 102
        self.image = Surface((WIDTH, HEIGHT))
        self.image = image.load("./img/monster_3.png")
        self.rect = Rect(x, y, WIDTH, HEIGHT) 