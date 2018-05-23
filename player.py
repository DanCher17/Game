#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame import *
from trampoline import *
from GameObject import *
import time

MOVE_SPEED = 5
JUMP_POWER = 10
GRAVITY = 0.35
ticks = pygame.time.get_ticks()

class Player(GameObject):
    SCORE = 0
    def __init__(self, x, y, boost):
        GameObject.__init__(self, x = x, y = y, width = 50, height = 50, image = image.load("./img/hero.png" ))
        self.xvel = 0
        self.yvel = 0 
        self.onGround = False
        self.boost = boost
        self.win = False

    def update(self, control, colliders):
        if control['right']:
            self.xvel = MOVE_SPEED
        if control['up']:
            self.yvel = -MOVE_SPEED 
        if control['down']:
            self.yvel = MOVE_SPEED 

        if not (control['right'] or control['up'] or control['down']):
            self.xvel = 0

        seconds = (pygame.time.get_ticks() - ticks) / 1000
        if not self.onGround:
            if seconds < 5:
                self.yvel +=  GRAVITY + self.boost
            else:
                self.yvel +=  GRAVITY

        if self.rect.x > 3500:
            self.win = True
            print("SCORE = " + str(self.SCORE))

        self.onGround = False;

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, colliders)

        self.rect.y += self.yvel
        self.collide(0, self.yvel, colliders)

    def collide(self, xvel, yvel, colliders):
            for gr in colliders[3]:
                if sprite.collide_rect(self, gr): 
                    if yvel > 0:               
                        self.rect.bottom = gr.rect.top 
                        self.onGround = True          
                        self.yvel = 0 
                    if yvel < 0:               
                        self.rect.top = gr.rect.bottom        
                        self.yvel = 0 

            monsters_hit_list = sprite.spritecollide(self, colliders[0], False)
            for mn in monsters_hit_list:
                if xvel > 0:
                    self.rect.right = mn.rect.left
                if yvel > 0:         
                    self.rect.bottom = mn.rect.top
                if yvel < 0:
                    self.rect.top = mn.rect.bottom

            stars_hit_list = sprite.spritecollide(self, colliders[1], True)
            for star in stars_hit_list:
                self.SCORE = self.SCORE + 5
            tramps_hit_list = sprite.spritecollide(self, colliders[2], False)
            for tramp in tramps_hit_list:
                tramp.tramp_animation()
                self.yvel = -JUMP_POWER

    
