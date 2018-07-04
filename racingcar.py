# ...................:
import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green =(0,255,0)

block_color=(53,115,255)

car_width = 70

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('CAR RACING')

clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')

def things_dodged(count):
    font=pygame.font.SysFont('italic',25)
    text=font.render("score:"+str(count),True,black)
    gameDisplay.blit(text,(0,0))

def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])



def car(x,y):
    gameDisplay.blit(carImg,(x,y))


'''def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(red)
        pixAr = pygame.PixelArray(gameDisplay)
        pixAr[10][20] = green
        pygame.draw.line(gameDisplay, blue, (0, 600), (0, 800), 5)
        pygame.display.update()

'''
def text_objects(text,font):
    textSurface=font.render(text,True,black)
    return textSurface,textSurface.get_rect()


def display_msg(text):
    largeText = pygame.font.Font("freesansbold.ttf",40)
    TextSurf,TextRect=text_objects(text,largeText)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()

    time.sleep(2)
    game_loop()

def crash():
    display_msg("bomm!! U CRASHED")

def game_loop():

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx=random.randrange(0,display_width)
    thing_starty=-600
    thing_speed=random.randrange(5,8)
    thing_width=100
    thing_height=100
    thingCount = 1

    dodged = 0

    Exit = False

    while not Exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pygame.draw.line(gameDisplay, blue, (0,display_width), (0, display_height), 5)
            pygame.display.update()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(red)

        things(thing_startx,thing_starty,thing_width,thing_height,block_color)
        thing_starty+=thing_speed
        car(x,y)

        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty>display_height:
            thing_starty=0-thing_height
            thing_startx=random.randrange(0,display_width)
            dodged+=2

            thing_speed+=1
            thing_width+=1

        if y < thing_starty+thing_height:
            print('y crossed')

            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print('x crossed')
                crash()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
