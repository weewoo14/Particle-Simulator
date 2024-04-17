import pygame
from pygame.locals import *
pygame.init()
# Text Initialization
font = pygame.font.SysFont('javanesetext',80,bold=True)
# Color Text
red = font.render("R",True,'white')
orange = font.render("O",True,'white')
yellow = font.render("Y",True,'white')
green = font.render("G",True,'white')
blue = font.render("B",True,'white')
purple = font.render("P",True,'white')
white = font.render("W",True,'black')
# Function Text
snowflake = font.render("SF",True,'white')
follow_mouse = font.render("FM",True,'white')
reverse_gravity = font.render("RG",True,'white')
start_text = font.render("Begin!",False,'white')
exit_text = font.render("Q",False,'white')
title_text = font.render("Particle Simulator",True,'white')