#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame import *

WIDTH = 50
HEIGHT = 50
STAR_IMG = "./img/star.png" 

class Star(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((WIDTH, HEIGHT))
        self.image = image.load(STAR_IMG)
        self.rect = Rect(x, y, WIDTH, HEIGHT)
