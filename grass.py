import random

from pico2d import *

class Grass:
    eat_sound = None

    def __init__(self):
        self.image = load_image('grass.png')
        self.bgm = load_music('Earthy_Crust.mp3')
        self.bgm.set_volume(60)
        self.bgm.repeat_play()
        if Grass.eat_sound == None:
            Grass.eat_sound = load_wav('warning.wav')
            Grass.eat_sound.set_volume(32)

    def draw(self):
        self.image.draw(400, -20)

    def draw_bb(self):
        #draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return 0,0,799,50

    def __del__(self):
        del self.image
        del self.bgm

    def eat(self, ball):
        self.eat_sound.play()


class Grass2:
    eat_sound = None

    def __init__(self):
        self.image = load_image('grass.png')
        self.bgm = load_music('Earthy_Crust.mp3')
        self.bgm.set_volume(60)
        self.bgm.repeat_play()
        if Grass.eat_sound == None:
            Grass.eat_sound = load_wav('warning.wav')
            Grass.eat_sound.set_volume(32)


    def draw(self):
        self.image.draw(400, -18)

    def draw_bb(self):
        #draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return 0,0,799,50

    def __del__(self):
        del self.image
        del self.bgm

    def eat(self, ball):
        self.eat_sound.play()





