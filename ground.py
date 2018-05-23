#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame import *
from GameObject import *

class Ground(GameObject):
     def __init__(self, x, y):
        GameObject.__init__(self, x = x, y = y, width = 32, height = 26, image = image.load("./img/ground.png"))
