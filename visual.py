import pygame, sys, random, time
from pygame.locals import *
from utils import *
import math
import constants

WINDOW_SIZE = 800

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
brown = (210,105,30)
light_green = (195, 250, 210)
light_grey = (214, 214, 214)
dark_grey = (66, 66, 66)

colors = {
    constants.EMPTY: light_grey,
    constants.WALL: dark_grey,
    constants.GOAL: light_green,
    constants.BOX: brown,
}

def draw_tiles(dis, smap, config, block_size):
    
    global colors

    dis.fill(colors[constants.WALL])

    for i in range(0, smap.shape[0]):
        for j in range(0, smap.shape[1]):
            tx = i * block_size
            ty = j * block_size
            pygame.draw.rect(dis, colors[smap[i,j]], [ty, tx, block_size, block_size])

    player_pos = config.player
    px = player_pos.x * block_size
    py = player_pos.y * block_size
    pygame.draw.rect(dis, blue, [py, px, block_size, block_size])

    boxes = set()

    for box_pos in config.boxes:
        bx = box_pos.x * block_size
        by = box_pos.y * block_size 
        pygame.draw.rect(dis, colors[constants.BOX], [by, bx, block_size, block_size])  

def play(smap, path):
    
    dis = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption('Sokoban by Dream Team Anal')
    
    game_over = False

    sq = max(smap.shape[0], smap.shape[1])
    block_size = math.floor(WINDOW_SIZE/sq)
    clock = pygame.time.Clock()
    game_speed = 60
    current_idx = 0

    pygame.init()
    font = pygame.font.Font('freesansbold.ttf', 20)

    while not game_over:
        # keys = pygame.key.get_pressed()
        # if keys[K_LEFT]:
        #     if current_idx > 0:
        #         current_idx -= 1
        # if keys[K_RIGHT]:
        #     if current_idx < len(path) - 1:
        #         current_idx += 1

        draw_tiles(dis, smap, path[current_idx], block_size)

        clock.tick(game_speed)

        text_to_display = "Moves: %d" % current_idx
        text = font.render(text_to_display, True, white)
        text.set_alpha(127)
        dis.blit(text, (10, 10))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if current_idx > 0:
                        current_idx -= 1
                elif event.key == pygame.K_RIGHT: 
                    if current_idx < len(path) - 1:
                        current_idx += 1
                    elif current_idx == len(path) - 1: 
                        game_over = True
                        continue
    
    pygame.quit()
    quit()
