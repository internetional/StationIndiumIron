import pygame, sys, random
from constants import *
from Area import *


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
areas = pygame.sprite.Group()

# fill groups
for x in range(1, WORLDWIDTH+1):
    for y in range(1, WORLDHEIGHT+1):
        Area(areas, (x,y), is_hidden=random.randint(0,1),
             is_base=random.randint(0,1))

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


if __name__ == "__main__":
    main()

