import pygame as pg

#build 2 dimensional array
_ = False
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 3, 3, 3, 3, _, _, _, 2, 2, 2, _, _, 1],
    [1, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, 1],
    [1, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, 1],
    [1, _, _, 3, 3, 3, 3, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 4, _, _, _, 4, _, _, _, _, _, _, _, 1],
    [1, 1, 3, 1, 3, 1, 1, 1, 3, 3, 3, 3, 1, 1, 1, 1],
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
        