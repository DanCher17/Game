#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame import *
from GameObject import *
import pyganim

TRAMP_ANIM = ["./img/trampoline/2.png"]

class Trampoline(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x = x, y = y, width = 58, height = 22, image = image.load("./img/trampoline/1.png"))

        Animation = []
        for anim in TRAMP_ANIM:
            Animation.append((anim, 0.008))
        self.Anim = pyganim.PygAnimation(Animation)
        self.Anim.play()

    def tramp_animation(self):
        self.image.fill(Color("#000000"))
        self.image.set_colorkey(Color("#000000"))
        self.Anim.blit(self.image, (0, 0))

