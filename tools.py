import os
import pygame as pg

mainDir = os.path.split(os.path.abspath(__file__))[0]
imgDir = os.path.join(mainDir, "images")


def loadImage(name, colorkey = None, scale = 1):
    fullname = os.path.join(imgDir, name)
    try:
        image = pg.image.load(fullname)
    except FileNotFoundError:
        print(f"Can't load image: {fullname}")
        raise SystemExit
    return image, image.get_rect()