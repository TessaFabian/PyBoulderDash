from pygame import sprite
from pygame import Rect
import pygame as pg



class AnimatedSprite(sprite.Sprite):
    def __init__(self, sprite_width, sprite_height, num_cols, num_rows):
        super().__init__()
        self.sprite_sheet = pg.image.load("images/boulderdash.png")
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height
        self.num_cols = num_cols
        self.num_rows = num_rows

        self.images = []
        for row in range(num_rows):
            for col in range(num_cols):
                x = col * self.sprite_width
                y = row * self.sprite_height
                image = self.sprite_sheet.subsurface(Rect(x, y, self.sprite_width, self.sprite_height))
                self.images.append(image)

        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.top_left = (100,100) #Position des Sprites auf der Surface
        self.currentframe = 0
        self.animationspeed = 0.1
        self.animation_time = 0

    def update(self, dt):
        self.animation_time += dt
        if self.animation_time >= self.animationspeed:
            self.animation_time = 0
            self.currentframe = (self.currentframe + 1)%len(self.images)
            self.image = self.images[self.currentframe]