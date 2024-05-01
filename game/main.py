import asyncio
import sys

import pygame

COLORS = [
    ['aliceblue', 'antiquewhite4', 'aquamarine4'],
    ['blueviolet', 'chocolate1', 'darksalmon'],
]
FPS = 25


async def main():
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode((1200, 800))
    clock = pygame.time.Clock()

    color_index_y = 0
    color_index_x = 0
    color_len_y = len(COLORS)
    color_len_x = len(COLORS[0])

    while True:  # EVENT LOOP
        for event in pygame.event.get():
            if not event.type == pygame.KEYUP:
                continue

            if event.key == pygame.K_a:
                color_index_x = (color_index_x - 1) % color_len_x
                new_color = COLORS[color_index_y][color_index_x]
                screen.fill(new_color)
                pygame.display.update()

            if event.key == pygame.K_d:
                color_index_x = (color_index_x + 1) % color_len_x
                new_color = COLORS[color_index_y][color_index_x]
                screen.fill(new_color)
                pygame.display.update()

            if event.key == pygame.K_s:
                color_index_y = (color_index_y - 1) % color_len_y
                new_color = COLORS[color_index_y][color_index_x]
                screen.fill(new_color)
                pygame.display.update()

            if event.key == pygame.K_w:
                color_index_y = (color_index_y + 1) % color_len_y
                new_color = COLORS[color_index_y][color_index_x]
                screen.fill(new_color)
                pygame.display.update()

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        clock.tick(FPS)  # Frames per second, 25 fps
        await asyncio.sleep(0)


if __name__ == '__main__':
    asyncio.run(main())
