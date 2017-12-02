import random

from pico2d import *
#from tile import load_tile_map


class Background:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 20.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.y = 0
        self.image =load_image('space1.png')


    def draw(self):
        self.image.draw(400,1721-self.y)
        self.image.draw(400,570-self.y)

    def update(self, frame_time):
        self.y = (self.y +frame_time*100) %1150


class Background2:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 20.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.y = 0
        self.image =load_image('space2.png')


    def draw(self):
        self.image.draw(400,1721-self.y)
        self.image.draw(400,570-self.y)

    def update(self, frame_time):
        self.y = (self.y +frame_time*100) %1150