import random
import os
import game_framework
from pico2d import *
import title_state
import random
from background import Background
from player import Player
from mob import BigMob
from grass import Grass
from grass import Grass2
from bullet import Bullet

bull1 = 0
delay_time =0
kill = 0
Life = 10
count = 0
speed = 1
name = "MainState"
grass = None
grass2 = None
font = None
background = None
player = None
mobs = None
big_mobs = None


def create_world():
    global player, grass, mobs, big_mobs,background,bullet,bullets, grass2

    player = Player()
    grass = Grass()
    bullet = Bullet()
    bullets = [Bullet() for i in range(10)]
    grass = Grass()
    grass2 = Grass2()
    background = Background()
    big_mobs = [BigMob() for i in range(410)]

    mobs = [Mob() for i in range(0)]
    mobs = big_mobs + mobs


def destroy_world():
    global player, mobs, grass,background,bullet,bullets,font, grass2
    del(bullet)
    del(bullets)
    del(player)
    del(mobs)
    del(background)
    del(grass)
    del(grass2)
    del(font)


def enter():
    global font
    font = load_font('ENCR10B.TTF')
    game_framework.reset_time()
    create_world()


def exit():
    pass


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    global x, y, count
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

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True



def update(frame_time):
    global Life,B,kill,speed,delay_time,bull1

    background.update(frame_time)

    for mob in mobs:
        mob.update(frame_time*speed)

    for mob in mobs:
        if collide(player, mob):
            mobs.remove(mob)
            kill = 0
            Life = 10
            speed = 1
            delay_time = 0
            game_framework.change_state(title_state)
            break;

        if collide(grass, mob):
            mobs.remove(mob)
            Life = (Life - 1)
            print(Life)
            if (Life % 10 == 0):
                kill = 0
                Life = 10
                speed = 1
                delay_time = 0
                game_framework.change_state(titlle_state)
                break;


    for mob in mobs:
        if collide(player, mob):
            mobs.remove(mob)
            kill = 0
            Life = 10
            speed = 1
            delay_time =0
            game_framework.change_state(title_state)
            break;


        if collide(grass2,mob):
            mobs.remove(mob)
            Life=(Life-1)
            print(Life)
            if(Life%10==0):
                kill = 0
                Life = 10
                speed = 1
                delay_time =0
                game_framework.change_state(title_state)
                break;


    for bul in bullets:
        for mob in mobs:
            if collide(bul, mob):
                if(kill<400):
                    if bul.life == True:
                        mobs.remove(mob)
                        kill = (kill+1)
                        print(kill)
                        bull1 = (bull1+1)
                        if(bull1==1):
                            bull1=0
                            bul.life = False
                elif(kill>=400):
                    delay_time =0
                    kill=0
                    Life = (Life+20)
                    speed = 1
                    game_framework.change_state(title_state)



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



    for mob in mobs:
        mob.draw()

    grass.draw()
    grass2.draw()
    player.draw()

    update_canvas()






