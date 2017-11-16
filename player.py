import random

from pico2d import *

class Player:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    print(RUN_SPEED_PPS)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8
    global x, y
    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = random.randint(0, 7)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.xdir, self.ydir = 0, 0
        self.state = self.RIGHT_STAND
        if Player.image == None:
            Player.image = load_image('playerShip2_red.png')


    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        self.life_time += frame_time
        distance = Player.RUN_SPEED_PPS * frame_time
        self.total_frames += Player.FRAMES_PER_ACTION * Player.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 1
        self.x += (self.xdir * distance)
        if self.x > 800:
            self.x=800
        if self.x < 0:
            self.x = 0
        self.y += (self.ydir * distance)
        if self.y > 600:
            self.y= 600
        if self.y < 0:
            self.y = 0


        if self.xdir == -1: self.state = self.LEFT_RUN
        elif self.xdir == 1: self.state = self.RIGHT_RUN
        elif self.xdir == 0:
            if self.state == self.RIGHT_RUN: self.state = self.RIGHT_STAND
            elif self.state == self.LEFT_RUN: self.state = self.LEFT_STAND



    def draw(self):
        self.image.opacify(random.random())
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)


    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 75, 50, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT: self.xdir += -2
            elif event.key == SDLK_RIGHT: self.xdir += 2
            elif event.key == SDLK_UP: self.ydir += 2
            elif event.key == SDLK_DOWN: self.ydir += -2
        if event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT: self.xdir += 2
            elif event.key == SDLK_RIGHT: self.xdir += -2
            elif event.key == SDLK_UP: self.ydir += -2
            elif event.key == SDLK_DOWN: self.ydir += 2


