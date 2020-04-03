import pygame as pg
import random
import numpy
import math
from settings import *
from sprites import *
import webbrowser
#Initializing the pygame library
pg.init()
#Set Caption to the window

pg.display.set_caption(gameName)


gameRunning = True
intro = True
class Game():

    def __init__(self):
        #initializing the game window
        pg.init()
        self.screen = pg.display.set_mode(SCREEN_DIM)
        pg.display.set_caption(gameName)
        self.clock = pg.time.Clock()
        self.running = True

    def game_menu(self):
        button_1 = pg.image.load("Drawables/start_game.png")
        button_2 = pg.image.load("Drawables/source_code.png")
        box_pointer = pg.image.load("Drawables/box_pointer.png")
        box_pointer_pos(40,90)

        button_12 = pygame.Rect(50, 100, 200, 50)
        self.button_12.fill(button_1)
        bg = pg.image.load("Drawables/background_vertical.png")

        self.screen.blit(bg,[0,0])
        self.screen.blit(button_1,(50,60))
        self.screen.blit(button_2,(50,150))
        self.screen.blit(box_pointer,box_pointer_pos)
        # self.screen.blit(img_new_game,[400,200])
        while intro:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_DOWN:
                        pass










            pg.display.flip()

    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        #self.screen.blit(self.base_platform,(0,HEIGHT-40))
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.all_sprites.add(self.player)
        self.run()
    def run(self):
        #mainloop of the program
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()
        #hits = pg.sprite.spritecollide(self.player,self.platforms,False)
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
        if self.player.rect.top <=HEIGHT/4:
            self.player.pos.y += abs(self.player.vel.y)
            for each in self.platforms:
                each.rect.y += abs(self.player.vel.y)
                if each.rect.top >= HEIGHT:     #Killing the platform once it crosses the bottom of the screen
                    each.kill()

        while len(self.platforms) < 6:
            width = random.randrange(50, 100)
            li = [
                pg.image.load('Drawables/platforms/01.png'),pg.image.load('Drawables/platforms/02.png'),pg.image.load('Drawables/platforms/03.png'),pg.image.load('Drawables/platforms/04.png')
            ]
            platform_respecitve_width = [74,50,80,90]
            platform_select = random.randrange(0,4)
            p = Platform(random.randrange(0, WIDTH-platform_respecitve_width[platform_select]),
                         random.randrange(-75, -30),li[platform_select])
            self.platforms.add(p)
            self.all_sprites.add(p)

    def game_over_screen(self):
        pass

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.player.jump()
    def draw(self):
        self.screen.blit(bg_image,(0,0))
        self.all_sprites.draw(self.screen)
        pg.display.flip()
g  = Game()
#g.game_menu()
g.running = True
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
