import pygame as pg

from tools import *
from locals import *
from world import *
from AnimatedSprite import *

class Player(AnimatedSprite):

    def __init__(self, width, height, num_columns, num_rows, start_x, start_y):
        super().__init__(width, height, num_columns, num_rows, start_x, start_y)
        self.speed_x = 0
        self.speed_y = 0

    def handle_input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.speed_x = -5
        elif keys[pg.K_RIGHT]:
            self.speed_x = 5
        elif keys[pg.K_UP]:
            self.speed_y = -5
        elif keys[pg.K_DOWN]:
            self.speed_y = 5
        else:
            self.speed_y = 0
            self.speed_x = 0
    
    def update(self, dt):
        self.handle_input()
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        super().update()
        #collision detection
        


    # def update(self, screen):

    #     walkCooldown = 5 # pass 5 iterations before increasing self.index in the animation part

    #     key = pg.key.get_pressed()
    #     if key[pg.K_LEFT]:
    #         self.rect.x -= 5
    #         self.counter += 1
    #         self.direction = -1
    #     if key[pg.K_RIGHT]:
    #         self.rect.x += 5
    #         self.counter += 1
    #         self.direction = 1
    #     if key[pg.K_LEFT] == False and key[pg.K_RIGHT] == False:
    #         self.counter = 0
    #         self.index = 0
    #         #player keeps his direction
    #         if self.direction == 1:
    #             self.image = self.imagesRight[self.index]
    #         if self.direction == -1:
    #             self.image = self.imagesLeft[self.index]
    #     if key[pg.K_UP]:
    #         self.rect.y -= 5
    #         self.direction = -2
    #     if key[pg.K_DOWN]:
    #         self.rect.y += 5
    #         self.direction = 2

    #     #handle animations
    #     if self.counter > walkCooldown:
    #         self.counter = 0
    #         self.index += 1
    #         if self.index >= len(self.imagesRight) and self.direction in (1,-1):
    #             print("links rechts")
    #             self.index = 1
    #         if self.direction == 1:
    #             self.image = self.imagesRight[self.index]
    #         if self.direction == -1:
    #             self.image = self.imagesLeft[self.index]
    #         if self.index >= len(self.imagesUp) and self.direction in (2,-2):
    #             print("oben unten")
    #             self.index = 1
    #         if self.direction == 2:
    #             print("oben unten")
    #             self.image = self.imagesDown[self.index]
    #         if self.direction == -2:
    #             print("oben unten")
    #             self.image = self.imagesUp[self.index]


    #     #check for collisions
    #     for tile in self.world.tile_list:
    #         tile_rect = tile[1]
    #         tileIsObstacle = tile[2]
    #         if tile_rect.colliderect(self.rect) and tileIsObstacle:
    #             if self.direction == 1: #Player bewegt sich nach rechts
    #                 self.rect.right = tile_rect.left
    #             elif self.direction == -1: #Player bewegt sich nach links
    #                 self.rect.left = tile_rect.right
    #             elif self.direction == -2: #Player bewegt sich nach oben
    #                 self.rect.top = tile_rect.bottom
    #             elif self.direction == 2: #Player bewegt sich nach unten
    #                 self.rect.bottom = tile_rect.top



    #     screen.blit(self.image, self.rect)
