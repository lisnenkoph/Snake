import pygame
import random
import time

pygame.init()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 25)

BLACK = (0, 0, 0)
RED = (209, 3, 3)
GREEN = (0, 255, 0)
YELLOW = (255, 200, 57)
CYAN = (110, 157, 64)
ORANGE = (239, 79, 79)
GOLD = (255, 215, 0)

dis = pygame.display.set_mode((540, 360))
pygame.display.set_caption('Dream team')

clock = pygame.time.Clock()

snake = 10
snake_speed = 12
accelerated_speed = 20

font_style = pygame.font.SysFont(None, 30)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [540 / 4, 360 / 4])

def scores(score):
    value = score_font.render(str(score), True, BLACK)
    dis.blit(value, [0, 0])

def snakes(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, ORANGE, [x[0], x[1], snake_block, snake_block])

def gameLoop():
    close = False
    over = False

    x = 270
    y = 180
