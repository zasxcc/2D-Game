import random
from pico2d import *
class Boss:
    image = None
    def __init__(self):
        if Boss.image == None:
            self.image = load_image('enemyBlack3.png')
        self.x, self.y = 500, 550
        self.speed = 100 # 200 pixel per second
        self.speed2 = 0 # 200 pixel per second

    def update(self, frame_time):
        self.x += frame_time * self.speed
        if self.x > 800:
            self.x = 800
            self.speed = -self.speed
        if self.x < 0:
            self.x = 0
            self.speed = -self.speed

        self.y+=(frame_time * self.speed)
        if self.y >550:
            self.y = 550
            self.speed2 = -self.speed2
        if self.y < 450:
            self.y = 450
            self.speed2 = -self.speed2



    def draw(self):
            self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())



    def get_bb(self):
        return self.x-100, self.y-50, self.x+100, self.y+50

