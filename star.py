#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame import *
from GameObject import *

class Star(GameObject):
    def __init__(self, x, y):
    	GameObject.__init__(self, x = x, y = y, width = 50, height = 50, image = image.load("./img/star.png"))

