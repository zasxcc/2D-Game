import random
import os
import game_framework
from pico2d import *
import title_state
import random
from background import Background
from player import Player # import player class from player.py
from mob import BigMob
from grass import Grass
from bullet import Bullet

bull1 = 0
delay_time =0
kill = 0
Life = 10
count = 0
count2 = 0
count3 = 0
speed = 1
name = "MainState"
grass = None
font = None
background = None
player = None
mobs = None
big_mobs = None


def create_world():
    global player, grass, mobs, big_mobs,background,bullet,bullets

    player = Player()
    grass = Grass()
    bullet = Bullet()
    bullets = [Bullet() for i in range(10)]
    grass = Grass()
    background = Background()
    big_mobs = [BigMob() for i in range(410)]

    mobs = [Mob() for i in range(0)]
    mobs = big_mobs + mobs


def destroy_world():
    global player, mobs, grass,background,bullet,bullets,font
    del(bullet)
    del(bullets)
    del(player)
    del(mobs)
    del(background)
    del(grass)
    del(font)


def enter():
    #open_canvas()
    global font
    font = load_font('ENCR10B.TTF')
    game_framework.reset_time()
    create_world()


def exit():
    #destroy_world()
    #close_canvas()
    pass


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    global x, y, count,count2,count3
    global Life,B,kill,speed,delay_time
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                kill = 0
                Life = 10
                count = 0
                speed = 1
                delay_time =0
                game_framework.change_state(title_state)


            if event.type == SDL_MOUSEBUTTONDOWN:
                if (event.button) == (SDL_BUTTON_LEFT):
                    x,y =player.x,player.y
                    if(True):
                        count=(count+1)%10
                        bullets[count].activate(player)

            else:
                player.handle_event(event)


def update(frame_time):
    global Life,B,kill,speed,delay_time,bull1

    background.update(frame_time)
    if(delay_time>13):
        for mob in mobs:
            mob.update(frame_time*speed)

    for obj in bullets:
        obj.update(frame_time*speed)

    delay_time = (delay_time+frame_time)
    player.update(frame_time)
    #delay(0.2)

def pause():
    pass

def draw(frame_time):
    clear_canvas()

    background.draw()

    for bul in bullets:
        if bul.life==True:
            bul.draw()


    if(delay_time>14):
        for mob in mobs:
            mob.draw()

    grass.draw()
    player.draw()
    #player.draw_bb()

    update_canvas()






