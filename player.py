#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame import *
from tramp import *
import time
import star

MOVE_SPEED = 5
JUMP_POWER = 10

WIDTH = 50
HEIGHT = 50
GRAVITY = 0.35
PLAYER_IMG = "./img/hero.png" 

ticks=pygame.time.get_ticks()

class Player(sprite.Sprite):
    SCORE = 0

    def __init__(self, x, y, boost):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0 
        self.onGround = False
        self.image = image.load(PLAYER_IMG)
        self.rect = Rect(x, y, WIDTH, HEIGHT)
        self.boost = boost
        self.win = False

    def update(self, right, up, down, ground, monsters, star, tramps):
        if right:
            self.xvel = MOVE_SPEED
        if up:
            self.yvel = -MOVE_SPEED 
        if down:
            self.yvel = MOVE_SPEED 

        if not (right or up or down):
            self.xvel = 0

        seconds = (pygame.time.get_ticks() - ticks) / 1000
        if not self.onGround:
            if seconds < 3:
                self.yvel +=  GRAVITY + self.boost
            else:
                self.yvel +=  GRAVITY


        if self.rect.x > 3500:
            self.win = True
            print("SCORE = " + str(self.SCORE))

        self.onGround = False;

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, ground, monsters, star, tramps)

        self.rect.y += self.yvel
        self.collide(0, self.yvel, ground, monsters, star, tramps)

    def collide(self, xvel, yvel, ground, monsters, stars, tramps):
            for gr in ground:
                if sprite.collide_rect(self, gr): 
                    if yvel > 0:               
                        self.rect.bottom = gr.rect.top 
                        self.onGround = True          
                        self.yvel = 0 
                    if yvel < 0:               
                        self.rect.top = gr.rect.bottom        
                        self.yvel = 0 

            monsters_hit_list = sprite.spritecollide(self, monsters, False)
            for mn in monsters_hit_list:
                if xvel > 0:
                    self.rect.right = mn.rect.left
                if yvel > 0:         
                    self.rect.bottom = mn.rect.top
                if yvel < 0:
                    self.rect.top = mn.rect.bottom

            stars_hit_list = sprite.spritecollide(self, stars, True)
            for star in stars_hit_list:
                self.SCORE = self.SCORE + 5

            tramps_hit_list = sprite.spritecollide(self, tramps, False)
            for tramp in tramps_hit_list:
                tramp.tramp_animation()
                self.yvel = -JUMP_POWER

    
