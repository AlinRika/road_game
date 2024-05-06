from pathlib import Path

import pygame as pg

CURRENT_FOLDER = Path(__file__).parent


def load_image(name):
    path = CURRENT_FOLDER / name
    return pg.image.load(path).convert()
