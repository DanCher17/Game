#!/usr/bin/env python
# -*- coding: utf-8 -*-
import helperspygame
import tmxreader
import time
import pygame
from pygame import *
from camera import *
from player import *
from loadLevel import *

pygame.init() 

WIN_WIDTH = 600 
WIN_HEIGHT = 400
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) 
FONT = pygame.font.SysFont("Consolas", 16)
CENTER_OF_SCREEN = WIN_WIDTH / 2, WIN_HEIGHT / 2

def main():
    print("Enter position: ")
    x = int(input())
    print("Enter boost: ")
    boost = int(input())

    screen = pygame.display.set_mode((DISPLAY)) 
    pygame.display.set_caption("GAME") 
    bg = Surface((WIN_WIDTH,WIN_HEIGHT))
    renderer = helperspygame.RendererPygame() 
    
    sprite_layers, items_for_show, colliders = loadLevel("level.tmx")

    control = {'right': False, 'up': False, 'down': False}
    
    hero = Player(x, 80, boost)
    items_for_show.add(hero)
    
    timer = pygame.time.Clock()

    camera = Camera(camera_configure, 3500, 320)
    white = pygame.Color('white')
    while not hero.win:
        timer.tick(60)

        for e in pygame.event.get():
            if e.type == QUIT:
                raise (SystemExit, "QUIT")
            if e.type == KEYDOWN and e.key == K_RIGHT:
               control['right'] = True
            if e.type == KEYDOWN and e.key == K_UP:
               control['up'] = True
            if e.type == KEYDOWN and e.key == K_DOWN:
               control['down'] = True

            if e.type == KEYUP and e.key == K_RIGHT:
               control['right'] = False
            if e.type == KEYUP and e.key == K_UP:
               control['up'] = False
            if e.type == KEYUP and e.key == K_DOWN:
               control['down'] = False

        for sprite_layer in sprite_layers:
            if not sprite_layer.is_object_group: 
                renderer.render_layer(screen, sprite_layer) 

        for e in items_for_show:
            screen.blit(e.image, camera.apply(e))

        camera.update(hero) 
        center_offset = camera.reverse(CENTER_OF_SCREEN)
        renderer.set_camera_position_and_size(center_offset[0], center_offset[1], WIN_WIDTH, WIN_HEIGHT, "center")
        hero.update(control, colliders) 

        score_text = FONT.render("Score = " + str(hero.SCORE), 1, white)
        screen.blit(score_text, (5, 30))

        pygame.display.update()     
        screen.blit(bg, (0,0))   

    final_text = FONT.render("FINISH! Your score is " + str(hero.SCORE), 1, white)
    screen.blit(final_text, (175, 30))
    pygame.display.update()
    time.wait(5000)

if __name__ == "__main__":
    main()


