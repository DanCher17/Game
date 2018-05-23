import helperspygame
import tmxreader
import pygame
from pygame import *
from monsters import *
from star import *
from ground import *
from trampoline import *

def loadLevel(name):
    tramps = pygame.sprite.Group()
    monsters = pygame.sprite.Group()
    stars = pygame.sprite.Group()
    entities = pygame.sprite.Group() 
    ground = []

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
        tr = Trampoline(x,y)
        tramps.add(tr)
        entities.add(tramps)
    for i in range(200):
        gr = Ground(i*32, 390)
        ground.append(gr)
        tp = Ground(i*32, 0)
        ground.append(tp)
    entities.add(ground)
    colliders = (monsters, stars, tramps, ground)

    return sprite_layers, entities, colliders