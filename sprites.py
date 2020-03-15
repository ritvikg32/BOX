# Sprite classes for platform game
import pygame as pg
from settings import *
vec = pg.math.Vector2
class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.box = box_img
        #self.rect = self.image.get_rect()
        #self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH/2,0)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0.5)

#To be called after calling the update function
    #def get_box_position(self):
     #    return self.pos


    def update(self):
        PLAYER_INITIAL_Y = 0
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.vel.y -= PLAYER_INITIAL_Y

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.pos.x -= PLAYER_VEL
        if keys[pg.K_RIGHT]:
            self.pos.x += PLAYER_VEL


        u=v
        self.pos.y = (u**2 - v**2)/2*(0.5)



        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH



        return (int(self.pos.x),int(self.pos.y))
        #Ties the camera with the position of the player
        #self.rect.midbottom = self.pos

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y