import random
from pico2d import *
class BigMob4:
    image = 0
    def __init__(self):
        if BigMob4.image == 0:
            self.image = load_image('dragon.png')
        self.x, self.y = 400, 500
        self.frame = 0
        self.speed = 100  # 200 pixel per second
        self.speed2 = 0  # 200 pixel per second

    def update(self, frame_time):
        self.x += frame_time * self.speed * 2
        self.frame = (self.frame + 1) % 2

        if self.x > 750:
            self.x = 750
            self.speed = -self.speed
        if self.x < 50:
            self.x = 50
            self.speed = -self.speed

        self.y += (frame_time * self.speed)
        if self.y > 500:
            self.y = 500
            self.speed2 = -self.speed2
        if self.y < 450:
            self.y = 450
            self.speed2 = -self.speed2

    def get_bb(self):
        return self.x - 100, self.y - 50, self.x + 100, self.y + 50

    def draw(self):
        num = 1
        if (num):
            self.image.clip_draw(self.frame * 200, 0, 200, 150, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

