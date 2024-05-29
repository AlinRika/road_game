import pygame as pg

from helper import load_image, calculate_start_object_position


#  start coordinates for first roads
START_ROAD_X = 160
START_ROAD_Y = 0


class Road(pg.sprite.Sprite):

    def __init__(self, offset, number_road, *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        self.image = load_image("road.gif")
        self.number_road = number_road
        self.offset = offset

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = calculate_start_object_position(
            START_ROAD_X,
            START_ROAD_Y,
            self.offset,
            self.number_road
        )
