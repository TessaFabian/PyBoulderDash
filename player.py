import pygame as pg

from tools import *
from locals import *

class Player(pg.sprite.Sprite):

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        #images moving to the right
        self.imagesRight = []
        self.imagesLeft = []
        self.index = 0 #index for the images in the animation list
        self.counter = 0 #controls the animation speed
        self.direction = 0 # direction the player is facing(1 right, -1 left)
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
        self.image = self.imagesRight[self.index] #player at his starting position
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


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
        if key[pg.K_DOWN]:
            self.rect.y += 5

        #handle animations
        if self.counter > walkCooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.imagesRight):
                self.index = 0
            if self.direction == 1:
                self.image = self.imagesRight[self.index]
            if self.direction == -1:
                self.image = self.imagesLeft[self.index]

        #check for collisions
        if HEIGHT - self.rect.bottom < 50:
            self.rect.bottom = HEIGHT - 50
        if self.rect.top < 50:
            self.rect.top = 50
        if self.rect.bottomleft[0] < 50:
            self.rect.bottomleft = (50, self.rect.bottomleft[1])
        if self.rect.bottomright[0] > WIDTH - 50:
            self.rect.bottomright = (WIDTH-50, self.rect.bottomright[1])


        screen.blit(self.image, self.rect)
