import pygame as pg
from pygame.locals import *

def main():
    pg.init()
    screen = pg.display.set_mode((1280, 780), pg.SCALED)
    pg.display.set_caption("Boulder Dash")

    background = pg.Surface(screen.get_size()).convert()
    background.fill((0,0,0))
    screen.blit(background, (0,0))


    pg.display.flip()
    clock = pg.time.Clock()

    running = True
    while running:
        clock.tick(60)

        for event in pg.event.get():
           if event.type == QUIT:
               running = False

        pg.display.flip()

if __name__ == "__main__": main()
