import sys
import pygame as pg
from settings import *
from map import *
from player import *

class Game:
    #create screen and set resolution from settings file
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()
    
    #new game method
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
    
    
    #update fram info on screen
    def update(self):
        self.player.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')
        
    
    
    #screen iteration
    def draw(self):
        self.screen.fill('black')
        self.map.draw()
        self.player.draw()
    #event for esc key
    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
                ):
                pg.quit()
                sys.exit()

    #run game method
    def run(self):
        while True:
            self.check_event()
            self.update()
            self.draw()

if  __name__ == '__main__':
    game = Game()
    game.run()