import pygame
gameName = 'BOX'
SCREEN_DIM = (412,600)
WIDTH = 412
HEIGHT = 600
FPS = 60

PLAYER_VEL = 0.2
PLAYER_ACC = 0.5     #Player's horizontal acceleration
PLAYER_VEL_Y = 0
PLAYER_GRAVITY = 0.5
PLAYER_FRICTION = -0.12
#Loading box image
box_img = pygame.image.load("Drawables/box_img_50x50.png")

#define COLORS
BLACK = (0, 0, 0)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#PLATFORM
WIDTH_PLATFORM = 50