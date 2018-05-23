import pygame
from pygame import *

class GameObject(sprite.Sprite):
    def __init__(self, x, y, width, height, image):
        sprite.Sprite.__init__(self)
        self.image = Surface((width, height))
        self.image = image
        self.rect = self.image.get_rect(x = x, y = y)
