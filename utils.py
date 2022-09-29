#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 16:20:12 2022

@author: rubem
"""
import pygame
from pygame.locals import *
from random import randint

width = 1000
height = 1000

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)

BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
WHITE = (255, 255, 255)

def draw_text(text, pos):
    img = font.render(text, True, BLACK)
    screen.blit(img, pos)

def random_point():
    x = randint(1, width)
    y = randint(1, height)
    return (x, y)

def random_points(n):
    points = []
    for i in range(n):
        p = random_point()
        points.append(p)
    return points

def random_rects(n):
    rects = []
    velocities = []
    for i in range(n):
        r = Rect(random_point(), (10, 10))
        rects.append(r)
        velocities.append([1,1])
    return rects,velocities

def wall_collision(rect,v):
    if rect.left < 0:
        v[0] *= -1
    if rect.right > width:
        v[0] *= -1
    if rect.top < 0:
        v[1] *= -1
    if rect.bottom > height:
        v[1] *= -1


pygame.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
running = True