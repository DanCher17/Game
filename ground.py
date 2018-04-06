#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame import *

WIDTH = 32
HEIGHT = 26
GROUND_IMG = "./img/ground.png" 
EXIT_IMG = "./img/exit.png" 

class Ground(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((WIDTH, HEIGHT))
        self.image = image.load(GROUND_IMG)
        self.rect = Rect(x, y, WIDTH, HEIGHT)
