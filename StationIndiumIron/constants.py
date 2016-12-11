from pygame.locals import *
from win32api import GetSystemMetrics

"""
A file containing all constants included in the program.
"""

# General
GAMENAME = "Station Indium-Iron"

# Display settings
FPS = 60
WINWIDTH = GetSystemMetrics(0)
WINHEIGHT = GetSystemMetrics(1)
GROUNDTHICKNESS = 20
MOUSEVISIBLE = True

# Colour palette
WHITE     = (255, 255, 255)
LIGHTGRAY = (189, 194, 191)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (156, 179,  28)
DARKGREEN = ( 59,  82,  73)
DARKGRAY  = ( 40,  40,  40)
GRAY      = ( 87,  96, 102)
DARKHAKI  = ( 86,  77,  74)
LIKHAKI   = (198, 173, 148)
PURPLE    = (119, 104, 133)
WINE      = ( 91,  35,  51)
PINK      = (250, 179, 169)
BONE      = (192, 183, 177)
ORANGE    = (222, 145,  81)
ZOMBIE    = (112, 135, 127)

# Tile design
TILESIZE = 20
TILECOLOUR = PURPLE
TILESPACE = 2
MOUSEOVERTILECOLOUR = LIKHAKI
TILESELECTCOLOUR = ORANGE
BASECOLOUR = ZOMBIE
BASESELECTCOLOUR = GREEN
MOUSEOVERBASECOLOUR = DARKGREEN

# World design
WORLDHEIGHT = 15
WORLDWIDTH  = 20
WORLDBGCOLOUR = DARKHAKI