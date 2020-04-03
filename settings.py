import pygame
gameName = 'BOX'

bg_image = pygame.image.load("Drawables/rsz_bg_vertical.jpg")
WIDTH = 412
HEIGHT = 600
SCREEN_DIM = (WIDTH,HEIGHT)
FPS = 60

PLAYER_VEL = 0.2
PLAYER_ACC = 0.5     #Player's horizontal acceleration
PLAYER_VEL_Y = 0
PLAYER_GRAVITY = 0.5
PLAYER_FRICTION = -0.12
#Loading box image
box_img = pygame.image.load("Drawables/Crate.png")

#define COLORS
BLACK = (0, 0, 0)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#platform sprites
all_sizes = [
    pygame.image.load('Drawables/platforms/01.png'), pygame.image.load('Drawables/platforms/02.png'),
    pygame.image.load('Drawables/platforms/03.png'), pygame.image.load('Drawables/platforms/04.png')

]
#PLATFORM
WIDTH_PLATFORM = 50
PLATFORM_LIST = [
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, all_sizes[3]),
                 (125, HEIGHT - 350, all_sizes[3]),
                 (350, 200, all_sizes[3]),
                 (175, 100, all_sizes[0])
]