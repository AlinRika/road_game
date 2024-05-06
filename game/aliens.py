import pygame as pg

from helper import load_image


class Alien(pg.sprite.Sprite):
    """An alien space ship. That moves by the roads."""

    def __init__(self, x_position, y_position, direction, *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        self.image = load_image("alien1.gif")
        self.rect = self.image.get_rect()

        self.rect.x = x_position
        self.rect.y = y_position
        self.direction = direction
        if self.direction:
            self.speed = -5
        else:
            self.speed = 5

        self.scene = pg.display.get_surface().get_rect()

    def update(self):
        self.rect.y += self.speed

    def fly_out(self):
        if self.rect.top > self.scene.bottom and not self.direction:
            return True
        if self.rect.bottom < self.scene.top and self.direction:
            return True
