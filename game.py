#!/usr/bin/env python
# -*- coding: utf-8 -*-
import helperspygame
import tmxreader
import time
import pygame
from pygame import *
from player import *
from monsters import *
from camera import *
from star import *
from tramp import *
from ground import *

pygame.init()

WIN_WIDTH = 600 
WIN_HEIGHT = 400
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) 
font = pygame.font.SysFont("Consolas", 16)
CENTER_OF_SCREEN = WIN_WIDTH / 2, WIN_HEIGHT / 2

def loadLevel(name):
    global playerX, playerY 
    global total_level_height, total_level_width
    global sprite_layers 

    world_map = tmxreader.TileMapParser().parse_decode(name)
    resources = helperspygame.ResourceLoaderPygame() 
    resources.load(world_map) 
    
    sprite_layers = helperspygame.get_layers_from_map(resources) 

    monsters_layer_1 = sprite_layers[0]
    for monster in monsters_layer_1.objects:
        x = monster.x
        y = monster.y
        mn = Monster_1(x,y)
        monsters.add(mn)
        entities.add(monsters)
    monsters_layer_2 = sprite_layers[1]
    for monster in monsters_layer_2.objects:
        x = monster.x
        y = monster.y
        mn = Monster_2(x,y)
        monsters.add(mn)
        entities.add(monsters)
    monsters_layer_3 = sprite_layers[2]
    for monster in monsters_layer_3.objects:
        x = monster.x
        y = monster.y
        mn = Monster_3(x,y)
        monsters.add(mn)
        entities.add(monsters)
    stars_layer = sprite_layers[3]
    for star in stars_layer.objects:
        x = star.x
        y = star.y
        st = Star(x,y)
        stars.add(st)
        entities.add(stars)
    tramps_layer = sprite_layers[4]
    for tramp in tramps_layer.objects:
        x = tramp.x
        y = tramp.y
        tr = Tramp(x,y)
        tramps.add(tr)
        entities.add(tramps)

    total_level_width  = 3500
    total_level_height = 320

def main():
    print("Enter position: ")
    x = int(input())
    print("Enter boost: ")
    boost = int(input())

    pygame.init() 
    screen = pygame.display.set_mode(DISPLAY) 
    pygame.display.set_caption("Duckin Ball") 
    bg = Surface((WIN_WIDTH,WIN_HEIGHT))
    renderer = helperspygame.RendererPygame() 
    loadLevel("level.tmx")

    right = False
    up = False
    down = False

    for i in range(200):
        gr = Ground(i*32, 390)
        ground.append(gr)
        tp = Ground(i*32, 0)
        ground.append(tp)
    entities.add(ground)

    hero = Player(x,80, boost)
    entities.add(hero)
    
    timer = pygame.time.Clock()

    camera = Camera(camera_configure, total_level_width, total_level_height)

    while not hero.win:
        timer.tick(60)
        for e in pygame.event.get():
            if e.type == QUIT:
                raise (SystemExit, "QUIT")
            if e.type == KEYDOWN and e.key == K_RIGHT:
               right = True
            if e.type == KEYDOWN and e.key == K_UP:
               up = True
            if e.type == KEYDOWN and e.key == K_DOWN:
               down = True

            if e.type == KEYUP and e.key == K_RIGHT:
               right = False
            if e.type == KEYUP and e.key == K_UP:
               up = False
            if e.type == KEYUP and e.key == K_DOWN:
               down = False

        for sprite_layer in sprite_layers:
            if not sprite_layer.is_object_group: 
                renderer.render_layer(screen, sprite_layer) 

        for e in entities:
            screen.blit(e.image, camera.apply(e))

        camera.update(hero) 
        center_offset = camera.reverse(CENTER_OF_SCREEN)
        renderer.set_camera_position_and_size(center_offset[0], center_offset[1], WIN_WIDTH, WIN_HEIGHT, "center")
        hero.update(right,up,down, ground, monsters, stars, tramps) 

        score_text = font.render("Score = " + str(hero.SCORE), 1, (255,255,255))
        screen.blit(score_text, (5, 30))

        pygame.display.update()     
        screen.blit(bg, (0,0))   

    final_text = font.render("FINISH! Your score is " + str(hero.SCORE), 1, (255,255,255))
    screen.blit(final_text, (175, 30))
    pygame.display.update()
    time.wait(5000)

ground = []
top = []
tramps = pygame.sprite.Group()
monsters = pygame.sprite.Group()
stars = pygame.sprite.Group()
entities = pygame.sprite.Group() 

if __name__ == "__main__":
    main()


