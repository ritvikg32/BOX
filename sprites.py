# Sprite classes for platform game
import pygame as pg
from settings import *
vec = pg.math.Vector2
class Player(pg.sprite.Sprite):
    def __init__(self,game):
        pg.sprite.Sprite.__init__(self)
        self.image = box_img
        self.game = game
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(350,180)
        self.vel = vec(0, 0)
        self.acc = vec(0, PLAYER_GRAVITY)

#To be called after calling the update function
    #def get_box_position(self):
     #    return self.pos

    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -20


    def update(self):

        self.acc = vec(0, PLAYER_GRAVITY)       #Gravity always acts


        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        if keys[pg.K_UP]:
            self.jump()


        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        #Adding gravity to the box



        #Sitting on the sprites condition
        #Make the accelation and the velocity of the box 0 when the box hits the platform


        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        if self.pos.y > HEIGHT:
            self.game.game_over_screen()
            

        #self.rect.center = self.pos
        #Ties the camera with the position of the player
        self.rect.midbottom = self.pos

    def gravity(self):
        self.acc.y = PLAYER_GRAVITY

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y,image):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        #self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #for x in range(0,HEIGHT/6,50)
        #self.x_cor = []
        #self.y_cor = []
        #self_pos = vec(self.x_cor,self.y_cor)


   # def update(self):

