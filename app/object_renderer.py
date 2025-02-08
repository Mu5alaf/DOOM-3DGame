import pygame as pg
from settings import * 
import os
base_path = os.path.join(os.path.dirname(__file__), 'media', 'textures')

class ObjectRenderer:
    def __init__(self,game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textuers()
        self.cloud_image = self.get_texture(os.path.join(base_path,'cloud.png'),(WIDTH, HALF_HEIGHT))
        self.cloud_offse = 0
    
    def draw(self):
        self.draw_background()
        self.render_game_objects()
    
    def draw_background(self):
        self.cloud_offse = (self.cloud_offse + 4.0 * self.game.player.rel) % WIDTH
        self.screen.blit(self.cloud_image,(-self.cloud_offse,0))
        self.screen.blit(self.cloud_image,(-self.cloud_offse + WIDTH,0))
        #floor
        pg.draw.rect(self.screen, FLOOR_COLOR,(0,HALF_HEIGHT,WIDTH,HEIGHT))
    
    def render_game_objects(self):
        list_objects = self.game.raycasting.objects_to_render
        for depth, image, pos in list_objects:
            self.screen.blit(image,pos)
    
    
    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    def load_wall_textuers(self):
        return {
            1: self.get_texture(os.path.join(base_path, '1.png')),
            2: self.get_texture(os.path.join(base_path, '2.png')),
            3: self.get_texture(os.path.join(base_path, '3.png')),
            4: self.get_texture(os.path.join(base_path, '4.png')),
            5: self.get_texture(os.path.join(base_path, '5.png')),
        }
        
