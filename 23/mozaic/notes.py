# -*- coding: utf-8 -*-
# Dette ser kanskje ut som tetris, men det er ikke noe særlig til spill...
# Det er allikevel visse spilleregler du bør fælge for å ikke gå deg vill...

# Se deg litt rundt og se hva du kan finne.

# Ingenting av det du ser er tilfeldig valgt,
# det er en tanke bak alt...

# LYKKE TIL! :D&4Æs


# 26 lengde x 20 høyde = 520
# mosaic = 12 x 8 = 96
import sys
import pygame
from pygame.locals import *
import turtle
import random
import time


def main():

    o0 = ['y', 'd', 'd', 'd', 'd', 'r', 'd', 'o', 't', 't', 't', 't', 'd', 'd', 'o', 'o', 'o', 'd', 'b', 'b', 'd', 'b', 'b', 'd', 'b', 'b']
    o1 = ['d', 'b', 'd', 'd', 'r', 'r', 'd', 'o', 'd', 'd', 'd', 'd', 'g', 'g', 'o', 'd', 'd', 'd', 'b', 'd', 'd', 'b', 'd', 'd', 'b', 'd']
    o2 = ['d', 'b', 'b', 'b', 'r', 'd', 'd', 'o', 'o', 'd', 'd', 'g', 'g', 'd', 'd', 'o', 'd', 'o', 'b', 'y', 'y', 'b', 'y', 'y', 'b', 'd']
    o3 = ['y', 'y', 'd', 'd', 'd', 'o', 'o', 'o', 'd', 'o', 'o', 'o', 'd', 'o', 'o', 'o', 'd', 'o', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd']
    o4 = ['d', 'd', 'o', 'd', 't', 'o', 'd', 'd', 'd', 'o', 'd', 'd', 'd', 'l', 'd', 'd', 'd', 'o', 'o', 'd', 'd', 'd', 'd', 'd', 'd', 'r']
    o5 = ['o', 'o', 'o', 'd', 't', 'd', 't', 'd', 'o', 'o', 'o', 'd', 'l', 'l', 'l', 'd', 'b', 'b', 'd', 'l', 'd', 'd', 'd', 'd', 'r', 'r']
    o6 = ['d', 'd', 'd', 'd', 't', 'd', 't', 'M', 'o', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'b', 'M', 'M', 'l', 'l', 'd', 'd', 'o', 'r', 'd']
    o7 = ['d', 'd', 'd', 'r', 't', 'd', 't', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'b', 'M', 'M', 'l', 'd', 'o', 'o', 'o', 'd', 'd']
    o8 = ['d', 'd', 'r', 'r', 'd', 'd', 't', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'd', 'd', 'l', 'd', 'd', 'g', 'g']
    o9 = ['y', 'y', 'r', 'd', 'o', 'o', 'o', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'd', 'l', 'l', 'l', 'g', 'g', 'd']
    t0 = ['d', 'd', 'd', 'd', 'o', 'd', 'd', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'b', 'b', 'd', 'd', 'd', 'd', 'r']
    t1 = ['d', 'd', 'd', 'o', 'o', 'o', 'd', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'b', 'd', 'b', 'd', 'd', 'r', 'r']
    t2 = ['y', 'd', 't', 'o', 'd', 'd', 'd', 'l', 'M', 'M', 'M', 'M', 'b', 'b', 'M', 'M', 'M', 'M', 'M', 'b', 'd', 'b', 'b', 'b', 'r', 'd']
    t3 = ['y', 'd', 't', 'd', 't', 'd', 'l', 'l', 'l', 'M', 'M', 'M', 'b', 'M', 'l', 'M', 'M', 'M', 'g', 'g', 'd', 'l', 'd', 'd', 'd', 'r']
    t4 = ['d', 'd', 't', 'd', 't', 'd', 'l', 'd', 'd', 'd', 'd', 'd', 'b', 'd', 'l', 'l', 'd', 'g', 'g', 'd', 'd', 'l', 'l', 'd', 'r', 'r']
    t5 = ['d', 'y', 't', 'd', 't', 'd', 'l', 'l', 'd', 'd', 'd', 'g', 'g', 'd', 'l', 'd', 'd', 'y', 'd', 'y', 'y', 'l', 'd', 'd', 'r', 'd']
    t6 = ['d', 'y', 'd', 'd', 't', 'd', 'l', 'd', 't', 'd', 'g', 'g', 'd', 'd', 'g', 'g', 'y', 'y', 'd', 'y', 'd', 'd', 't', 't', 't', 't']
    t7 = ['d', 't', 't', 't', 't', 'd', 'b', 'd', 't', 'd', 'y', 'd', 'o', 'g', 'g', 'd', 'd', 'd', 'd', 't', 't', 't', 't', 'd', 'd', 'd']
    t8 = ['y', 'y', 'd', 'd', 'd', 'd', 'b', 'd', 't', 'd', 'y', 'd', 'o', 'd', 'd', 'l', 'd', 'd', 'g', 'g', 'd', 'd', 'd', 'y', 'd', 'y']
    t9 = ['y', 'd', 'y', 'd', 'd', 'b', 'b', 'd', 't', 'd', 'y', 'd', 'o', 'o', 'l', 'l', 'l', 'g', 'g', 'd', 'y', 'd', 'y', 'y', 'd', 'y']

    # t4 = ['','','','','','','','','','','','','','','','','','','','','','','','','','']
    alllines = []

    alllines = [o0, o1, o2, o3, o4, o5, o6, o7, o8, o9, t0, t1, t2, t3, t4, t5, t6, t7, t8, t9]
    red = 0
    blue = 0
    turkis = 0
    green = 0
    lilla = 0
    orange = 0
    dark = 0
    mosiac = 0

    for line in alllines:
        for letter in line:
            if letter == 'r':
                red += 1
            if letter == 'b':
                blue += 1
            if letter == 't':
                turkis += 1
            if letter == 'g':
                green += 1
            if letter == 'l':
                lilla += 1
            if letter == 'o':
                orange += 1
            if letter == 'd':
                dark += 1
            if letter == 'M':
                mosiac += 1
    #print(red, blue, turkis, green, lilla, orange, dark, mosiac)

    pygame.init()

    def setColors(alllines):
        linecounter = 0
        DISPLAY = pygame.display.set_mode((780, 600), 0, 32)
        WHITE = (255, 255, 255)
        blue = (0, 0, 255)
        red = (255, 0, 0)
        green = (0, 255, 0)
        turkis = (64, 244, 208)
        yellow = (255, 255, 0)
        orange = (255, 165, 0)
        dark = (65, 65, 65)
        mosiac = (1, 1, 1)
        lilla = (128, 0, 128)
        colors = [blue, red, green, turkis, yellow, orange, lilla]
        DISPLAY.fill(mosiac)
        for line in alllines:
            itemcounter = 0
            for item in line:
                if item == 'b':
                    item = blue
                if item == 'r':
                    item = red
                if item == 'g':
                    item = green
                if item == 't':
                    item = turkis
                if item == 'y':
                    item = yellow
                if item == 'o':
                    item = orange
                if item == 'd':
                    item = mosiac
                if item == 'M':
                    item = mosiac
                if item == 'l':
                    item = lilla
                # if item != mosiac and item != dark:
                    #item = random.choice(colors)
                pygame.draw.rect(DISPLAY, item, (itemcounter * 30, linecounter * 30, 29, 29))
                itemcounter += 1
            linecounter += 1

    # BLUE = (0, 0, 255)
    #pygame.draw.rect(DISPLAY, BLUE, (0, 0, 30, 30))

    while True:
        setColors(alllines)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == "__main__":
    main()
