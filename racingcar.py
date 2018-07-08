# ...................:
import pygame
import time
import random
import sqlite3
import tkinter
from tkinter import *

conn = sqlite3.connect('racing.db')
print("database opened successfully!")
a="select * from scored"
conn.execute(a)
conn.commit()
#conn.execute('''create table scored(
#SRNO INT AUTO INCREMENT NOT NULL,
#SCORE INT NOT NULL
#);
#''')


print("tables created!")

pygame.init()

# crash_sound =pygame.mixer.music.load('crashsound.wav')

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
bright_blue = (0, 0, 150)
bright_green = (0, 150, 0)
bright_red = (200, 0, 0)
block_color = (53, 115, 255)
grey = (120, 120, 120)
car_width = 70


# to make input in center x axis yaxis
#def geting():
 #   conn.execute("INSERT INTO score(SRNO,SCORE) VALUES(count.get())")


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


# carImg = pygame.image.load('lamb.jpg')

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('CAR RACING')

gameicon = pygame.image.load('lamb.jpg')
pygame.display.set_icon(gameicon)
clock = pygame.time.Clock()

carImg = pygame.image.load('car1.png')
gameDisplay.blit(carImg, (250, 380))

pause = False


def things_dodged(count):
    font = pygame.font.SysFont('italic', 25)
    text = font.render("score:" + str(count), True, red)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh):
    carImg = pygame.image.load('racecar.png')
    gameDisplay.blit(carImg, (thingx, thingy, thingw, thingh))


#    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def things1(thingx, thingy, thingw, thingh):
    carImg = pygame.image.load('racecar.png')
    gameDisplay.blit(carImg, (thingx, thingy, thingw, thingh))


def boundary(thingx, thingy, thingw, thingh, color):
    pygame.draw.line(gameDisplay, blue, (0, display_width), (0, display_height), 5)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == 'play':
                game_loop()
            elif action == 'quit':
                pygame.quit()
               # geting()
                quit()

    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    if click[0] == 1 and action != None:
        if action == 'unpause':
            unpause()
    # if click[0]==1 and action!=None:
    #        if action =='details':
    #           it()

    smallText = pygame.font.Font("freesansbold.ttf", 15)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2), (y + (h / 2))))
    gameDisplay.blit(textSurf, textRect)


'''def game_details():

    details = True

    while details:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)


        largeText = pygame.font.Font("freesansbold.ttf",60)
        TextSurf, TextRect = text_objects("CAR RACE", largeText)
        TextRect.center = ((400), (200))
        gameDisplay.blit(TextSurf, TextRect)

        carImg3 = pygame.image.load('i3.jpg')
        gameDisplay.blit(carImg3, (50, 100, 400, 400))

        button("ENTER YOUR NAME",200,300,200,50,green,bright_green,'details')
        button("QUIT", 500,300,100, 50, red,bright_red,'quit')
        pygame.display.update()

        clock.tick(30)
'''


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)

        largeText = pygame.font.Font("freesansbold.ttf", 60)

        TextSurf, TextRect = text_objects("CAR RACE", largeText)
        TextRect.center = ((400), (200))
        gameDisplay.blit(TextSurf, TextRect)

        r = conn.execute('''select max(SCORE) from scored''')
        conn.commit()
        #TextSurf, TextRect = text_objects(largeText)
        #TextSurf, TextRect = text_objects(str(r),largeText)
        #TextRect.center = ((400), (300))
        #gameDisplay.blit(TextSurf, TextRect)

        carImg1 = pygame.image.load('lamb.jpg')
        gameDisplay.blit(carImg1, (200, 300))

        button("START", 200, 300, 100, 50, green, bright_green, 'play')
        button("QUIT", 500, 300, 100, 50, red, bright_red, 'quit')
        pygame.display.update()

        clock.tick(30)


def unpause():
    global pause
    pygame.mixer.music.unpause()

    pause = False


def paused():
    pygame.mixer.music.pause()

    largeText = pygame.font.Font("freesansbold.ttf", 20)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width / 2), (250))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
        button("Continue", 210, 350, 100, 50, green, bright_green, 'unpause')
        button("QUIT", 500, 350, 100, 50, red, bright_red, 'quit')

        pygame.display.update()
        clock.tick(30)


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def text_objects1(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def display_msg(text):
    largeText = pygame.font.Font("freesansbold.ttf", 40)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)
    game_loop()


def crash():
    #    pygame.mixer.Sound.play('crashsound.wav')
    pygame.mixer.music.stop()
    while True:

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)

        button("Play Again", 150, 300, 100, 50, green, bright_green, 'play')
        button("Quit", 550, 300, 100, 50, red, bright_red, 'quit')

        largeText = pygame.font.Font("freesansbold.ttf", 40)
        TextSurf, TextRect = text_objects("You Crashed", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(30)


def game_loop():
    global pause

    pygame.mixer.music.load('crash.wav')
    pygame.mixer.music.play(-1)

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing1_startx = random.randrange(100, 600)
    thing1_starty = -600
    thing1_speed = random.randrange(6, 8)
    thing1_width = 70
    thing1_height = 70
    thing_startx = random.randrange(100, 600)
    thing_starty = -600
    thing_speed = random.randrange(6, 8)
    thing_width = 70
    thing_height = 70

    thingCount = 1

    dodged = 0

    Exit = False

    while not Exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # pygame.draw.line(gameDisplay, blue, (0, display_width), (0, display_height), 5)

            pygame.display.update()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                if event.key == pygame.K_RIGHT:
                    x_change = 10
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(grey)
        pygame.draw.line(gameDisplay, white, (100, 0), (100, 700), 5)
        pygame.draw.line(gameDisplay, white, (700, 0), (700, 700), 5)
        pygame.draw.line(gameDisplay, white, (400, 50), (400, 150), 5)
        pygame.draw.line(gameDisplay, white, (400, 50), (400, 150), 5)
        pygame.draw.line(gameDisplay, white, (400, 400), (400, 500), 5)
        trees = pygame.image.load('bush.png')
       # gameDisplay.blit(trees, (50, 50))
        #gameDisplay.blit(trees, (40, 150))
        things1(thing1_startx, thing1_starty, thing1_width, thing1_height)
        thing1_starty += thing1_speed

        things(thing_startx, thing_starty, thing_width, thing_height)
        thing_starty += thing_speed

        car(x, y)

        things_dodged(dodged)
        things_dodged(dodged)

        if x > (display_width - 100) - car_width or x < 100:
            crash()

        if thing1_starty > display_height:
            thing1_starty = 0 - thing1_height
            thing1_startx = random.randrange(100, 600)

            dodged += 1
            thing1_speed += 2
            # thing1_width+=1

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(100, 600)
            dodged += 1

            thing_speed += 2
            # thing_width+=1

        if y < thing1_starty + thing1_height or y < thing_starty + thing_height:
            print('y crossed')

            if x > thing1_startx and x < thing1_startx + thing1_width or x + car_width > thing1_startx and x + car_width < thing1_startx + thing1_width or (
                    x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width):
                print('x crossed')
                crash()
        pygame.display.update()
        clock.tick(30)


# game_details()
game_intro()
game_loop()
pygame.quit()
quit()
