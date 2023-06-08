FPS = 30
WINWIDTH = 640
WINHEIGHT = 480
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)

GRASSCOLOR = (24, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

CAMERASLACK = 90 #how far from the center the squirrel moves before moving the camera
MOVERATE = 9 #how fast the player moves
BOUNCERATE = 6 #how fast the player bounces (large is slower)
BOUNCEHEIGHT = 30 # how big the player bounces
STARTSIZE = 25 #how big the player starts off
WINSIZE = 300 #HOW BIG THE PLAYER NEEDS TO BE TO WIN
INVULNTIME = 2 # how long the player is invulnerable after beign hit in seconds
GAMEOVERTIME = 4 #how long the game over text says on the screen in seconds

MAXHEALTH = 3 #how much health the player starts with

NUMGRASS = 80 # number of grass objects in the active area
NUMSQUIRRELS = 30 # NUMBER OF SQUIRRELS IN THE ACTIVE AREA
SQUIRRELMINSPEED = 3 #slowest squirrel speed
SQUIRRELMAXSPEED = 7 #FASTEST SQUIRREL SPEED
DIRCHANGEFREQ = 2 #% CHANCE OF DIRECTION CHANGE PER FRAME
LEFT = 'left'
RIGHT = 'right' 