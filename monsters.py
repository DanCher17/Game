#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame import *
from GameObject import *

class Monster_1(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x = x, y = y, width = 94, height = 107, image = image.load("./img/monster_1.png"))

class Monster_2(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x = x, y = y, width = 65, height = 89, image = image.load("./img/monster_2.png"))

class Monster_3(GameObject):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        GameObject.__init__(self, x = x, y = y, width = 87, height = 102, image = image.load("./img/monster_3.png"))