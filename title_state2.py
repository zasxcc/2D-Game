import game_framework
from pico2d import *


import main_state


name = "TitleState2"
image = None
font1 =None

def enter():
    global image,font1
    image = load_image('title2.png')
    font1 = load_font('ENCR10B.TTF',30)

def exit():
    global image
    del(image)


def pause():
    pass

def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)




def update(frame_time):
    pass


def draw(frame_time):
    global image
    clear_canvas()

    image.draw(400, 300)
    font1.draw(180, 100, "Press SPACE To NEXT STAGE", (255,255,255))
    update_canvas()



