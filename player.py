import pygame as pg

from tools import *
from locals import *
from world import *

class Player(pg.sprite.Sprite):

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        #images moving to the right
        self.imagesRight = []
        self.imagesLeft = []
        self.imagesUp = []
        self.imagesDown = []
        self.index = 0 #index for the images in the animation list
        self.counter = 0 #controls the animation speed
        self.direction = 0 # direction the player is facing(1 right, -1 left)
        #Bilder laden, links und rechts
        for number in range(1,12):
            if number < 10:
                imgRight = pg.transform.scale(pg.image.load("images/player0" + str(number) + ".png"),
                    (50, 50))
                imgLeft = pg.transform.flip(imgRight, True, False)
            if number >= 10:
                imgRight = pg.transform.scale(pg.image.load("images/player" + str(number) + ".png"),
                    (50, 50))
                imgLeft = pg.transform.flip(imgRight, False, False)
            self.imagesRight.append(imgRight)
            self.imagesLeft.append(imgLeft)
        #Bilder laden, up und down
        for number in range(0,5):
            if number == 0:
                img = pg.transform.scale(pg.image.load("images/player20.png"),(50,50))
                self.imagesUp.append(img)
                self.imagesDown.append(img)
            elif number >= 1:
                img = pg.transform.scale(pg.image.load("images/player2"+str(number)+".png"),(50,50))
                self.imagesUp.append(img)
                self.imagesDown.append(pg.transform.flip(img, False, False))

        self.image = self.imagesRight[self.index] #player at his starting position
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.world = World()

    def update(self, screen):

        walkCooldown = 5 # pass 5 iterations before increasing self.index in the animation part

        key = pg.key.get_pressed()
        if key[pg.K_LEFT]:
            self.rect.x -= 5
            self.counter += 1
            self.direction = -1
        if key[pg.K_RIGHT]:
            self.rect.x += 5
            self.counter += 1
            self.direction = 1
        if key[pg.K_LEFT] == False and key[pg.K_RIGHT] == False:
            self.counter = 0
            self.index = 0
            #player keeps his direction
            if self.direction == 1:
                self.image = self.imagesRight[self.index]
            if self.direction == -1:
                self.image = self.imagesLeft[self.index]
        if key[pg.K_UP]:
            self.rect.y -= 5
            self.direction = -2
        if key[pg.K_DOWN]:
            self.rect.y += 5
            self.direction = 2

        #handle animations
        if self.counter > walkCooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.imagesRight):
                self.index = 1
            if self.direction == 1:
                self.image = self.imagesRight[self.index]
            if self.direction == -1:
                self.image = self.imagesLeft[self.index]

        #check for collisions
        for tile in self.world.tile_list:
            tile_rect = tile[1]
            tileIsObstacle = tile[2]
            if tile_rect.colliderect(self.rect) and tileIsObstacle:
                if self.direction == 1: #Player bewegt sich nach rechts
                    self.rect.right = tile_rect.left
                elif self.direction == -1: #Player bewegt sich nach links
                    self.rect.left = tile_rect.right
                elif self.direction == -2: #Player bewegt sich nach oben
                    self.rect.top = tile_rect.bottom
                elif self.direction == 2: #Player bewegt sich nach unten
                    self.rect.bottom = tile_rect.top



        screen.blit(self.image, self.rect)
