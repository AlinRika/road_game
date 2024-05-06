import pygame as pg

from helper import load_image


class Road(pg.sprite.Sprite):

    def __init__(self, x_position, y_position, *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        self.image = load_image("road.gif")
        self.rect = self.image.get_rect().move(x_position, y_position)

        self.rect.x = x_position
        self.rect.y = y_position
