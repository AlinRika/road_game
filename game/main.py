import asyncio
import sys
import time

import pygame as pg
from pygame.font import Font

from aliens import Alien
from helper import load_image
from player import Player
import random
from road import Road


FPS = 40
SCREEN_SIZE = (1280, 720)

START_ROAD_X = 160
START_ROAD_Y = 0
NUMBER_ROADS = 4

ALIEN_RELOAD = 40  # frames between new aliens
ALIEN_ODDS = 15  # chances a new alien appears
START_ALIEN_COORDINATES = ((160, -71), (240, 720))

OFFSET = 320


async def main():
    pg.init()
    screen: pg.Surface = pg.display.set_mode(SCREEN_SIZE)
    clock = pg.time.Clock()

    font = Font(None, 36)

    background = pg.Surface(screen.get_size()).convert()
    background_imgs = [load_image("background3.png"), load_image("dead.gif")]
    background.blit(background_imgs[0], (0, 0))

    screen.fill('black')

    alienreload = [
        [random.randint(0, ALIEN_RELOAD), random.randint(0, ALIEN_RELOAD)]
        for _ in range(4)
    ]

    all_objects = pg.sprite.RenderUpdates()
    aliens = pg.sprite.Group()
    roads = pg.sprite.Group()

    for i in range(NUMBER_ROADS):
        Road(START_ROAD_X + OFFSET * i, START_ROAD_Y, roads, all_objects)

    player = Player(all_objects)

    score = 0
    border_for_score = OFFSET

    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            player.move(up=True)
        if keys[pg.K_s]:
            player.move(down=True)
        if keys[pg.K_a]:
            player.move(left=True)
        if keys[pg.K_d]:
            player.move(right=True)

        screen.blit(background, (0, 0))

        # Create new alien
        for road_number in range(len(alienreload)):
            for road_direction in range(len(alienreload[road_number])):
                if alienreload[road_number][road_direction]:
                    alienreload[road_number][road_direction] -= 1
                elif not int(random.random() * ALIEN_ODDS):
                    start_alien_x, start_alien_y = START_ALIEN_COORDINATES[road_direction]
                    Alien(
                        start_alien_x + OFFSET * road_number,
                        start_alien_y,
                        road_direction,
                        aliens, all_objects
                    )
                    alienreload[road_number][road_direction] = ALIEN_RELOAD

        all_objects.draw(screen)
        aliens.update()

        aliens_collided = pg.sprite.spritecollide(player, aliens, False)
        if aliens_collided:
            background.blit(background_imgs[1], (0, 0))
            screen.blit(background, (0, 0))
            pg.display.update()
            time.sleep(2)
            pg.quit()
            sys.exit()

        if player.rect.left > border_for_score or (player.rect.x == 0 and border_for_score == screen.get_width()):
            score += 1
            border_for_score += OFFSET
        if border_for_score > screen.get_width():
            border_for_score = OFFSET

        text = font.render(f'Score: {score}', True, 'black')
        screen.blit(text, (10, 10))

        for alien in aliens:
            if alien.fly_out():
                alien.kill()

        pg.display.update()

        clock.tick(FPS)
        await asyncio.sleep(0)


if __name__ == '__main__':
    asyncio.run(main())
