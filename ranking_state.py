import game_framework
from pico2d import *


import title_state
import json


name = "RankingState"
image = None
font = None
font1 = None


def enter():
    global image,font,font1
    image = load_image('backboard.png')
    font = load_font('HYNAMB.TTF')
    font1 = load_font('HYNAMB.TTF',50)

def exit():
    global image,font,font1
    del(image)
    del(font)
    del(font1)


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

                game_framework.change_state(title_state)



def update(frame_time):
    pass


def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400, 300)

    with open('score.txt', 'r') as f:
        score_list = json.load(f)
    score_list.sort(reverse = True)

    top10 = score_list[:10]

    i=1
    font1.draw(300, 530, "Ranking", (255,255,255))
    for score in top10:
        font.draw(200, 500 - i * 30, "#%2d [Score = %d, kill=%d , Life= %d]" %(i,score[0],score[1],score[2]), (255,255,255))
        i+=1
    font1.draw(150, 100, "Press ESC To Continue", (255,255,255))

    update_canvas()



