import pygame, sys
from constants import *
from Area import *


# Game initiation
pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
pygame.display.set_caption(GAMENAME)
pygame.mouse.set_visible(MOUSEVISIBLE)

# variables
run_program = True
mouse_coord = (0, 0)

# groups
areas = pygame.sprite.Group()

# fill groups
for x in range(1, 11):
    for y in range(1, 11):
        Area(areas, (x,y))

def main():
    while run_program:
        # titleScreen()
        
        
        for event in pygame.event.get():
            eventHandler(event)

        DISPLAYSURF.fill(GRAY)
        areas.draw(DISPLAYSURF)
        areas.update()
        
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
    global run_program
    
    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
        run_program = False
        
    # player actions
    if event.type == KEYDOWN:
        print("KEYDOWN")
            
    if event.type == KEYUP:
        print("KEYUP")


if __name__ == "__main__":
    main()

