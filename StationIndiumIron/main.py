import pygame, sys, random
from constants import *
from Map import *


# Game initiation
pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT),
                                      pygame.FULLSCREEN)
pygame.display.set_caption(GAMENAME)
pygame.mouse.set_visible(MOUSEVISIBLE)

# variables
run_program = True
mouse_coord = (0, 0)


# groups
map = Map()
areas = map.areas

# fill groups
tiles = load_map("TestMap.txt")
[Area(*[areas]+x) for x in tiles]

def main():
    while run_program:
        # titleScreen()
        
        
        for event in pygame.event.get():
            eventHandler(event)

        DISPLAYSURF.fill(WORLDBGCOLOUR)
        areas.draw(DISPLAYSURF)
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)
    
    terminate()

def terminate():
    pygame.quit()
    sys.exit()

def eventHandler(event):
    """
    Takes user events from pygame as input and executes associated
    actions. 
    
    """
    global run_program, mouse_coord
    
    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
        run_program = False
        
    # player actions
    if event.type == KEYDOWN:
        print("KEYDOWN")
            
    if event.type == KEYUP:
        print("KEYUP")

    if event.type == MOUSEMOTION:
        mouse_coord = event.pos
        areas.update(mouse_coord)

    if event.type == MOUSEBUTTONDOWN:
        areas.update(mouse_coord, True)



