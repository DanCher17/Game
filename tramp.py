#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame import *
import pyganim

WIDTH = 58
HEIGHT = 123
TRAMP_IMG = "./img/tramp_anim2.png" 
TRAMP_ANIM = ["./img/tramp_anim2.png",
"./img/tramp_anim1.png", 
"./img/tramp.png",
"./img/tramp_anim2.png"
]
ANIM_DELAY = 0.9

class Tramp(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.startX = x
        self.startY = y
        self.image = Surface((WIDTH,HEIGHT))
        self.rect = Rect(x, y, WIDTH, HEIGHT)
        self.image = image.load(TRAMP_IMG)

        Animation = []
        for anim in TRAMP_ANIM:
            Animation.append((anim, ANIM_DELAY))
        self.Anim = pyganim.PygAnimation(Animation)
        self.Anim.play()

    def tramp_animation(self):
        self.image.fill(Color("#000000"))
        self.image.set_colorkey(Color("#000000"))
        self.Anim.blit(self.image, (0, 0))
        


