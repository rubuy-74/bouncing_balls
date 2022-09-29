#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 16:11:42 2022

@author: rubem
"""

from utils import *
import random
num = 100
# rect = Rect(coords, (50, 50))
# v = [0.5,0.5]
rects,velocities = random_rects(num)
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                rects, velocities = random_rects(num)
        if event.type == QUIT:
            running = False
    screen.fill(GRAY)
    for c in range(num):
        pygame.draw.rect(screen, RED, rects[c])
        rects[c].move_ip(velocities[c])
        wall_collision(rects[c], velocities[c])
        if pygame.Rect.collidelist(rects[c], rects[:c]+rects[c+1:]) != -1:
            velocities[c][0] *= -1
            velocities[c][1] *= -1
    pygame.display.flip()
    

pygame.quit()