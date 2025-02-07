import pygame as pg

#build 2 dimensional array
_ = False
X = True
mini_map = [
    [X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X],
    [X, _, _, _, _, _, _, _, _, _, _, _, _, _, _, X],
    [X, _, _, X, X, X, X, _, _, _, X, X, X, _, _, X],
    [X, _, _, _, _, _, X, _, _, _, _, _, X, _, _, X],
    [X, _, _, _, _, _, X, _, _, _, _, _, X, _, _, X],
    [X, _, _, X, X, X, X, _, _, _, _, _, _, _, _, X],
    [X, _, _, _, _, _, _, _, _, _, _, _, _, _, _, X],
    [X, _, _, X, _, _, _, X, _, _, _, _, _, _, _, X],
    [X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X],
]


class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()
        
    #iterate the mini map
    def get_map(self):
        for x,row in enumerate(self.mini_map):
            for i,value in enumerate(row):
                if value:
                    self.world_map[(i,x)] = value
    
    #draw dimensional on screen
    def draw(self):
        [pg.draw.rect(
            self.game.screen, 'darkgray',
            (
                pos[0] * 100,
                pos[1] * 100, 100, 100
            ),2)
        for pos in self.world_map]
        