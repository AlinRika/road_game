import asyncio
import sys
import time
import random

import pygame as pg
from pygame.font import Font

from aliens import Alien
from helper import load_image, collided, calculate_background_index
from player import Player
from road import Road


# game constants
FPS = 40
SCREEN_SIZE = (1280, 720)

NUMBER_ROADS = 4  # number of roads on the map

ALIEN_RELOAD = 40  # frames between new aliens
ALIEN_ODDS = 15  # chances a new alien appears

OFFSET = 320  # total offset for game objects


async def main():
    # initialize pygame
    pg.init()
    screen: pg.Surface = pg.display.set_mode(SCREEN_SIZE)
    clock = pg.time.Clock()

    # set the display
    background = pg.Surface(screen.get_size()).convert()
    background_imgs = [load_image("background1.png"), load_image("background2.png"),
                       load_image("background3.png"), load_image("dead.gif")]
    background.blit(background_imgs[0], (0, 0))
    screen.fill('black')

    # initialize Game Groups
    all_objects = pg.sprite.RenderUpdates()
    aliens = pg.sprite.Group()
    roads = pg.sprite.Group()

    # set the text
    font = Font(None, 36)

    # list to control the appearance of aliens on different roads
    alien_reload = [
        [random.randint(0, ALIEN_RELOAD), random.randint(0, ALIEN_RELOAD)]
        for _ in range(4)
    ]

    # initialize our starting sprites
    for i in range(NUMBER_ROADS):
        Road(OFFSET, i, roads, all_objects)
    player = Player(all_objects)

    # create Starting Values for score
    score = 0
    border_for_score = OFFSET  # boundary that the player must cross in order to get a score +1

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

        # create new alien
        for number_road in range(len(alien_reload)):
            for road_direction in range(len(alien_reload[number_road])):
                if alien_reload[number_road][road_direction]:
                    alien_reload[number_road][road_direction] -= 1
                elif not int(random.random() * ALIEN_ODDS):
                    Alien(
                        OFFSET,
                        number_road,
                        road_direction,
                        aliens, all_objects
                    )
                    alien_reload[number_road][road_direction] = ALIEN_RELOAD

        # check a collision between a player and an alien
        aliens_collided = pg.sprite.spritecollide(player, aliens,  False, collided)
        if aliens_collided:
            background.blit(background_imgs[-1], (0, 0))
            screen.blit(background, (0, 0))
            text = font.render(f'Your score: {score}', True, 'black')
            screen.blit(text, (10, 10))
            pg.display.update()
            time.sleep(3)
            pg.quit()
            sys.exit()

        # improve the score
        if player.rect.left > border_for_score or (player.rect.x == 0 and border_for_score == screen.get_width()):
            score += 1
            border_for_score += OFFSET
        if border_for_score > screen.get_width():
            border_for_score = OFFSET
            background_index = calculate_background_index(score)
            background.blit(background_imgs[background_index], (0, 0))

        # draw the scene
        screen.blit(background, (0, 0))
        all_objects.draw(screen)
        aliens.update()
        # draw the score
        text = font.render(f'Score: {score}', True, 'black')
        screen.blit(text, (10, 10))
        # update display
        pg.display.update()

        # destruction of aliens that go beyond the playing field
        for alien in aliens:
            if alien.fly_out():
                alien.kill()

        clock.tick(FPS)
        await asyncio.sleep(0)


if __name__ == '__main__':
    asyncio.run(main())
