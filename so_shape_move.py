#https://stackoverflow.com/questions/68011629/how-do-you-write-a-function-in-pygame-that-draws-one-or-more-objects?rq=3
#! /usr/bin/env python3

import pygame
from random import uniform

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pygame .init()

origin = 0, 0
size = width, height = 400, 300
screen = pygame .display .set_mode( size )
pygame .display .set_caption( 'Jitter' )

white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
black = 0, 0, 0

background = pygame .Surface( screen .get_size() )
background = background .convert()
background .fill( white )

red_pos, red_size = ( 50, 50 ),  ( 50, 50 )  ##  left, top,  width, height
green_pos, green_size = ( 190, 130 ),  ( 20, 20 )
blue_pos, blue_size = ( 300, 50 ),  ( 50, 50 )
black_pos, black_size = ( 50, 220 ),  ( 300, 20 )

red_rect = pygame .Rect( red_pos, red_size )
green_rect = pygame .Rect( green_pos, green_size )
blue_rect = pygame .Rect( blue_pos, blue_size )
black_rect = pygame .Rect( black_pos, black_size )

def update_positions():  ##  move "in-place", as opposed to creating a new object
    red_rect .move_ip( uniform(-2, 2),  0 )
    green_rect .move_ip( 0,  uniform(-2, 2) )
    blue_rect .move_ip( uniform(-2, 2),  0 )
    black_rect .move_ip( uniform(-2, 2),  0 )

def draw_stuff():
    pygame .draw .rect( screen,  red,  red_rect )
    pygame .draw .rect( screen,  green,  green_rect )
    pygame .draw .rect( screen,  blue,  blue_rect )
    pygame .draw .rect( screen,  black,  black_rect )

run = True
while run:
    for event in pygame .event .get():
        if event .type == pygame .QUIT:
            pygame .quit()
            run = False

    screen .blit( background, origin )
    update_positions()
    draw_stuff()
    pygame .display .flip()

##  eof  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~