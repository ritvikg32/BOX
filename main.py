import pygame as pg
import numpy
import math
from settings import *
#Initializing the pygame library
pg.init()
#Set Caption to the window

pg.display.set_caption(gameName)

gameDisplay = pg.display.set_mode(SCREEN_DIM)

gameRunning = True
intro = True
class Game():

    def __init__(self):
        #initializing the game window
        pg.init()
        self.screen = pg.display.set_mode(SCREEN_DIM)
        pg.display.set_caption(gameName)
        #self.clock = pg.time.clock()
        self.running = True
    def new(self):
        pass
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
            img_new_game = pg.image.load("Drawables\\test_new.png")
            bg = pg.image.load("Drawables\\menu_background.png")
            self.screen.blit(bg,[0,0])
            self.screen.blit(img_new_game,[400,200])

            pg.display.flip()

    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass
    def run(self):
        #mainloop of the program
        self.playing = True
        while self.playing:
            #self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        pass
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False
    def draw(self):
        self.screen.fill(WHITE)
        #self.all_sprites.draw(self.screen)
        pg.display.flip()
g  = Game()
g.game_menu()
g.show_start_screen()
g.running = True
while g.running:
    g.run()
    g.show_go_screen()

pg.quit()



