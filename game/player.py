import pygame as pg

from helper import load_image

# Start coordinates for player
START_PLAYER_X = 55
START_PLAYER_Y = 325


class Player(pg.sprite.Sprite):
    """Representing the player as a little pink piggy."""

    speed = 10

    def __init__(self, *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        self.image = load_image("player2.gif")
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect().move(START_PLAYER_X, START_PLAYER_Y)

        self.scene = pg.display.get_surface().get_rect()

    def move(self, up=False, down=False, left=False, right=False):
        if right:
            if self.rect.right > self.scene.right:
                self.rect.x = 0
            else:
                self.rect.x += self.speed
        if left:
            if self.rect.left < self.scene.left:
                self.rect.x += 0
            else:
                self.rect.x -= self.speed
        if down:
            if self.rect.bottom > self.scene.bottom:
                self.rect.y += 0
            else:
                self.rect.y += self.speed
        if up:
            if self.rect.top < self.scene.top:
                self.rect.y += 0
            else:
                self.rect.y -= self.speed


