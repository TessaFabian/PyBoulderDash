
import pygame as pg
from pygame.locals import *
from locals import *
from player import Player
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
    player = Player(50, HEIGHT-100)
    running = True
    while running:

        clock.tick(FPS)

        world.draw(screen)
        player.update(screen)
        #draw_grid(screen)

        for event in pg.event.get():
           if event.type == QUIT:
               running = False

        pg.display.update()

    pg.quit()

if __name__ == "__main__": main()
