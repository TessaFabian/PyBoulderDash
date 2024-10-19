import pygame as pg
from tools import *
from locals import *

class Player(pg.sprite.Sprite):

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = loadImage("boulderdash.png").convert()
