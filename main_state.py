import random
import os
import game_framework
from pico2d import *
import title_state
import title_state2
import random
import ranking_state
from background import Background
from background import Background2
from player import Player
from mob import BigMob
from mob import BigMob2
from grass import Grass
from grass import Grass2
from bullet import Bullet
from bullet import Bullet2


bull1 = 0
bull2 = 0
delay_time =0
kill = 1
Life = 10
count = 0
speed = 1
stage = 1
name = "MainState"
grass = None
grass2 = None
font = None
background = None
background2 = None
player = None
mobs = None
mobs2 = None
big_mobs = None
big_mobs2 = None
score = 0


def create_world():
    global player, grass,stage, mobs,mobs2, big_mobs,big_mobs2, background,background2, bullet,bullets,bullet2, bullets2, grass2, score

    player = Player()
    grass = Grass()
    bullet = Bullet()
    bullets = [Bullet() for i in range(10)]
    bullet2 = Bullet2()
    bullets2 = [Bullet2() for i in range(10)]
    grass = Grass()
    grass2 = Grass2()
    background = Background()

    if (stage == 1):
        grass2 = Grass2()
        grass = Grass()
        background = Background()
        background2 = False
        big_mobs = [BigMob() for i in range(410)]
        big_mobs2 = [BigMob2() for i in range(0)]


    if (stage == 2):
        grass2 = Grass2()
        grass = Grass()
        background = False
        background2 = Background2()
        big_mobs = [BigMob() for i in range(0)]
        big_mobs2 = [BigMob2() for i in range(510)]


    mobs = [Mob() for i in range(0)]
    mobs = big_mobs + mobs

    mobs2 = [Mob2() for i in range(0)]
    mobs2 = big_mobs2 + mobs2



def destroy_world():
    global player, mobs,mobs2, grass,background,bullet,bullets,bullet2, bullets2, font,grass2
    del(bullet)
    del(bullet2)
    del(bullets)
    del(bullets2)
    del(player)
    del(mobs)
    del(mobs2)
    del(background)
    del(grass)
    del(grass2)
    del(font)


def enter():
    global font
    font = load_font('ENCR10B.TTF')
    game_framework.reset_time()
    create_world()


def record_score():
    #read previous data
    with open('score.txt', 'r') as f:
        score_list = json.load(f)

    # add new score
    score_list.append([score,kill,Life])
    #write all the scores
    with open('score.txt', 'w') as f:
       json.dump(score_list , f)


def exit():
    pass


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    global x, y, count
    global Life,B,kill,speed,delay_time, score
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


            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
                x,y =player.x,player.y
                if(score < 10000):
                    count=(count+1)%10
                    bullets[count].activate(player)
                if(score>=10000):
                    count = (count + 1) % 10
                    bullets2[count].activate(player)

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
    global Life,B,kill,speed,delay_time,bull1, bull2, stage,score


    if (stage == 1):
        background.update(frame_time)

        for mob in mobs:
            mob.update(frame_time * speed)

    elif (stage == 2):
        background2.update(frame_time)

        for mob2 in mobs2:
            mob2.update(frame_time * speed)

    for mob in mobs:
        if collide(player, mob):
            record_score()
            mobs.remove(mob)
            kill = 0
            Life = 10
            speed = 1
            stage = 1
            score= 0
            delay_time = 0
            game_framework.change_state(ranking_state)
            break

        if collide(grass, mob):
            mobs.remove(mob)
            Life = (Life - 1)
            print(Life)
            if (Life % 10 == 0):
                record_score()
                kill = 0
                Life = 10
                score = 0
                speed = 1
                stage = 1
                delay_time = 0
                game_framework.change_state(ranking_state)
                break


    for mob in mobs:
        if collide(player, mob):
            record_score()
            mobs.remove(mob)
            kill = 0
            Life = 10
            speed = 1
            stage=1
            score = 0
            delay_time =0
            game_framework.change_state(ranking_state)
            break

        if collide(grass2,mob):
            record_score()
            mobs.remove(mob)
            Life=(Life-1)
            print(Life)
            if(Life%10==0):
                kill = 0
                Life = 10
                speed = 1
                score = 0
                stage = 1
                delay_time =0
                game_framework.change_state(ranking_state)
                break


    for mob2 in mobs2:
        if collide(player, mob2):
            mobs2.remove(mob2)
            record_score()
            kill = 0
            Life = 10
            speed = 1
            stage = 1
            score = 0
            delay_time =0
            game_framework.change_state(ranking_state)
            break

        if collide(grass,mob2):
            mobs2.remove(mob2)
            Life=(Life-1)
            print(Life)
            if(Life%10==0):
                record_score()
                kill = 0
                Life = 10
                speed = 1
                score = 0
                stage = 1
                delay_time =0
                game_framework.change_state(ranking_state)
                break


    for bul in bullets:
        for mob in mobs:
            if collide(bul, mob):
                if(kill<400):
                    if bul.life == True:
                        mobs.remove(mob)
                        kill = (kill+1)
                        print(kill)
                        score = (score+100)
                        bull1 = (bull1+1)
                        if(bull1==1):
                            bull1=0
                            bul.life = False
                elif (kill >= 400):
                    delay_time = 0
                    kill = 0
                    speed = 1
                    stage = 2
                    record_score()
                    game_framework.change_state(title_state2)

    for bul in bullets:
        for mob2 in mobs2:
            if collide(bul, mob2):
                if(kill<400):
                    if bul.life == True:
                        mobs2.remove(mob2)
                        kill = (kill+1)
                        score = (score+200)
                        print(kill)
                        bull1 = (bull1+1)
                        if(bull1==1):
                            bull1=0
                            bul.life = False
                elif (kill >= 400):
                    delay_time = 0
                    kill = 0
                    speed = 1
                    stage = 2
                    record_score()
                    game_framework.change_state(title_state2)



    for bul2 in bullets2:
        for mob in mobs:
            if collide(bul2, mob):
                if(kill>0):
                    if bul2.life == True:
                        mobs.remove(mob)
                        score = (score + 100)
                        print(kill)
                        bull2 = (bull2+1)
                        if(bull2==2):
                            bull2=0
                            bul2.life = False
                elif (kill >= 400):
                    delay_time = 0
                    kill = 0
                    speed = 1
                    stage = 2
                    record_score()
                    game_framework.change_state(title_state2)


    for bul2 in bullets2:
        for mob2 in mobs2:
            if collide(bul2, mob2):
                if(kill>0):
                    if bul2.life == True:
                        mobs2.remove(mob2)
                        score = (score+200)
                        print(kill)
                        bull2 = (bull2+1)
                        if(bull2==2):
                            bull2=0
                            bul2.life = False
            elif (kill >= 400):
                delay_time = 0
                kill = 0
                speed = 1
                stage = 2
                record_score()
                game_framework.change_state(title_state2)



    if (score < 10000):
        for obj in bullets:
            obj.update(frame_time * speed)
    if (10000 <= score):
        for obj in bullets2:
            obj.update(frame_time * speed)

    delay_time = (delay_time+frame_time)
    player.update(frame_time)
    #delay(0.3)

def pause():
    pass

def draw(frame_time):
    clear_canvas()

    if(stage==1):
        background.draw()
    elif(stage==2):
        background2.draw()

    if(score<10000):
        for bul in bullets:
            if bul.life==True:
                bul.draw()
    if(10000<=score):
        for bul2 in bullets2:
            if bul2.life==True:
                bul2.draw()

    for mob in mobs:
        mob.draw()

    for mob2 in mobs2:
        mob2.draw()

    grass.draw()
    grass2.draw()
    player.draw()


    font.draw(600, 50, "score = %d" %score, (255,255,255))
    font.draw(600, 70, "Life = %d" %Life, (255,255,255))

    update_canvas()






