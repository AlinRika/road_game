from pathlib import Path

import pygame as pg

CURRENT_FOLDER = Path(__file__).parent


def load_image(name):
    """load new image from a file (or file-like object), convert and return it"""
    path = CURRENT_FOLDER / name
    return pg.image.load(path).convert()


def calculate_start_object_position(x_coordinate, y_coordinate, offset, number_road):
    """calculate a start coordinates for game objects (road, alien) and return it"""
    x_position = x_coordinate + offset * number_road
    y_position = y_coordinate
    return x_position, y_position


# this callback function is passed as the `collided`argument to pygame.sprite.spritecollide.
def collided(sprite, other):
    """Check if the hitboxes of the two sprites collide."""
    return sprite.hitbox.colliderect(other.hitbox)