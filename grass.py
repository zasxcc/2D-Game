import random

from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')


    def draw(self):
        self.image.draw(400, -20)


    def __del__(self):
        del self.image
