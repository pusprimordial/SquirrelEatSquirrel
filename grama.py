import pygame, time
from pygame.locals import *

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, L_PLAYER_IMG, R_PLAYER_IMG, GRASSIMAGES

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode(WINWIDTH, WINHEIGHT)
    pygame.display.set_caption('GRAMA')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 32)


    #load image files
    L_PLAYER_IMG = pygame.image.loa('./')
    R_PLAYER_IMG = pygame.transform.flip(L_PLAYER_IMG, True, False)
    GRASSIMAGES = []
    for i in range(1, 5):
        GRASSIMAGES.append(pygame.image.load('./'))
    while True:
        runGame()

def runGame():

    #camerax and cameray are where the middle of the camera view is
    camerax = 0
    cameray = 0

    grassObjs= [] #store all the grass objects in the game

    #stores the player object:
    playerObj = {'surface': pygame.transform.scale(L_SQUIR_IMG,(STARTSIZE, STARTSIZE)),
                 'facing': LEFT,
                 'size': STARTSIZE,
                 'x': HALF_WINWIDTH,
                 'y': HALF_WINHEIGHT,
                 'bounce':0,
                 'health': MAXHEALTH}
    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False

    
    



