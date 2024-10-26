import pygame
import pygame as pg
from pygame.locals import *
from locals import *
from world import *

pg.init()

#range(0,38)?
#WIDTH/TILE_SIZE = 38
def draw_grid(screen):
    for line in range(0,38):
        pg.draw.line(screen, WHITE, (0,line*TILE_SIZE), (WIDTH, line*TILE_SIZE))
        pg.draw.line(screen, WHITE, (line * TILE_SIZE, 0), (line * TILE_SIZE, HEIGHT))

def main():
    screen = pg.display.set_mode((WIDTH, HEIGHT), pg.SCALED)

    pg.display.set_caption("Boulder Dash")

    clock = pg.time.Clock()

    world = World()

    running = True
    while running:

        world.draw(screen)

        draw_grid(screen)

        for event in pg.event.get():
           if event.type == QUIT:
               running = False

        pg.display.update()

    pygame.quit()

if __name__ == "__main__": main()
