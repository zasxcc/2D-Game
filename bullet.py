import random

from pico2d import *

class Bullet:
    def __init__(self):
        self.x, self.y = 0, 0
        self.image1 = load_image('laserblue01.png')
        self.speed = 100
        self.life = False


    def activate(self, player):
        self.x, self.y = player.x,player.y+50
        self.life = True

    def update(self, frame_time):
        if self.y <620:
            self.y += self.speed/5
            self.y+=20
        if self.y >620:
            self.y = 0
            self.x = -50
            self.y += self.speed/5
            self.y-= 20

    def draw(self):
        if(self.life):
            self.image1.clip_draw(0, 0, 20, 30, self.x, self.y)


