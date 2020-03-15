import pygame as pg
import numpy
import math
from sprites import *
from settings import *
#Initializing the pygame library
pg.init()
#Set Caption to the window

pg.display.set_caption(gameName)

gameDisplay = pg.display.set_mode((WIDTH,HEIGHT))

gameRunning = True
intro = True

class Game():

    def __init__(self):
        #initializing the game window
        pg.init()
        self.icon = pg.image.load("Drawables\\main_logo.png")
        pg.display.set_icon(self.icon)
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(gameName)
        #self.clock = pg.time.clock()
        self.running = True
    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        #self.walls = pg.sprite.Group()
        #self.mobs = pg.sprite.Group()
        #self.bullets = pg.sprite.Group()
        # for row, tiles in enumerate(self.map.data):
        #     for col, tile in enumerate(tiles):
        #         if tile == '1':
        #             Wall(self, col, row)
        #         if tile == 'M':
        #             Mob(self, col, row)
        #         if tile == 'P':
        #             self.player = Player(self, col, row)


        #self.camera = Camera(self.map.width, self.map.height)

    def game_menu(self):
        while intro:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()



            #Background image
            img_new_game = pg.image.load("Drawables\\test_new.png")
            bg = pg.image.load("Drawables\\menu_background_1024x768.png")
            self.screen.blit(bg,[0,0])

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
        #self.player = Player
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False
    def draw(self):
        self.screen.fill(WHITE)
        curr_pos = player.update()
        self.screen.blit(box_img, curr_pos)
        #self.all_sprites.draw(self.screen)
        pg.display.flip()


player = Player()
g  = Game()
g.run()
#g.new()
#g.game_menu()
g.running = True
while g.running:
    g.run()
    g.show_go_screen()

pg.quit()



