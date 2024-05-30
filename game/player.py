import pygame as pg

from helper import load_image

# Start coordinates for player
START_PLAYER_POSITION = (80, 360)


class Player(pg.sprite.Sprite):
    """Representing the player as a little pink piggy."""

    speed = 10

    def __init__(self, *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        self.image = load_image("player1.gif")
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=START_PLAYER_POSITION)
        self.hitbox = self.rect.inflate(-15, -12)

        self.scene = pg.display.get_surface().get_rect()

    def move(self, up=False, down=False, left=False, right=False):
        if right:
            if self.rect.right < self.scene.right:
                self.rect.x += self.speed
                self.hitbox.x += self.speed
            else:
                self.rect.x = 0
                self.hitbox.x = 0
        if left:
            if self.rect.left > self.scene.left:
                self.rect.x -= self.speed
                self.hitbox.x -= self.speed
        if down:
            if self.rect.bottom < self.scene.bottom:
                self.rect.y += self.speed
                self.hitbox.y += self.speed
        if up:
            if self.rect.top > self.scene.top:
                self.rect.y -= self.speed
                self.hitbox.y -= self.speed
