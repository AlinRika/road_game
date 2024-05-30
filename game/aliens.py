import pygame as pg

from helper import load_image, calculate_start_object_position


START_ALIEN_COORDINATES = ((200, -71), (280, 720))  # start coordinates for firsts aliens


class Alien(pg.sprite.Sprite):
    """An alien spaceship. That moves by the roads."""

    def __init__(self, offset, number_road, direction, *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        self.offset = offset
        self.number_road = number_road
        self.direction = direction

        pos = calculate_start_object_position(
            START_ALIEN_COORDINATES[self.direction][0],
            START_ALIEN_COORDINATES[self.direction][1],
            self.offset,
            self.number_road,
        )

        self.image = load_image("alien1.gif")
        self.rect = self.image.get_rect(center=pos)
        self.hitbox = self.rect.inflate(-15, -12)

        if self.direction:
            self.speed = -5
        else:
            self.speed = 5

        self.scene = pg.display.get_surface().get_rect()

    def update(self):
        self.rect.y += self.speed
        self.hitbox.y += self.speed

    def fly_out(self):
        """return True if alien went beyond the boundary of the playing field"""
        if self.rect.top > self.scene.bottom and not self.direction:
            return True
        if self.rect.bottom < self.scene.top and self.direction:
            return True
