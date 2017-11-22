import random

from pico2d import *

class BigMob:
    image = 0
    def __init__(self):
        self.x, self.y = random.randint(15, 785), random.randint(500, 1500)
        self.fall_speed = random.randint(200,300)
        if BigMob.image == 0:
            BigMob.image = load_image('enemyBlack1.png')


    def update(self, frame_time):
            self.y -= frame_time * self.fall_speed/10


    def draw(self):
            self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())




