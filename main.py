import pygame as pg
import random
import numpy
import math
from settings import *
from sprites import *
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
        while intro:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if img_new_game.get_rect().collidepoint(x, y):
                        self.run()
            #Background image
            img_new_game = pg.image.load("Drawables/test_new.png")
            bg = pg.image.load("Drawables/menu_background.png")
            self.screen.blit(bg,[0,0])
            self.screen.blit(img_new_game,[400,200])

            pg.display.flip()

    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.platform = Platform(WIDTH,HEIGHT/4.5,WIDTH/4,25)
        self.platforms.add(self.platform)
        self.all_sprites.add(self.platform)
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
        hits = pg.sprite.spritecollide(self.player,self.platforms,False)
        if hits:
            self.player.pos.y = hits[0].rect.top
            self.player.vel.y = 0
        if self.player.rect.top <=HEIGHT/4:
            self.player.pos.y += abs(self.player.vel.y)
            for each in self.platforms:
                each.rect.y += abs(self.player.vel.y)
                if each.rect.top >= HEIGHT:     #Killing the platform once it crosses the bottom of the screen
                    each.kill()

        while len(self.platforms) < 4:
            width = random.randrange(50, 100)
            p = Platform(random.randrange(0, WIDTH/2),
                         random.randrange(-75, -70),
                         width, 10)
            self.platforms.add(p)
            self.all_sprites.add(p)
    '''
    def start_game_setup(self):
        for plat_no in range(7):
            plat = Platform()
    '''

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.player.jump()
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()
g  = Game()
#g.game_menu()
g.running = True
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()



