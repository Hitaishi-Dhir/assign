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
bright_blue=(0,0,150)
bright_green=(0,150,0)
bright_red = (200,0,0)
block_color=(53,115,255)

car_width = 70

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('CAR RACING')

clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')
pause=False

def things_dodged(count):
    font=pygame.font.SysFont('italic',25)
    text=font.render("score:"+str(count),True,red)
    gameDisplay.blit(text,(0,0))

def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])



def car(x,y):
    gameDisplay.blit(carImg,(x,y))


def button(msg,x,y,w,h,ic,ac,action=None):
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        print(click)
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
            if click[0]==1 and action !=None:
                if action == 'play':
                    game_loop()
                elif action == 'quit':
                    pygame.quit()
                    quit()

        else:
            pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

        if click[0]==1 and action !=None:
                if action == 'unpause':
                    unpause()

        smallText = pygame.font.Font("freesansbold.ttf", 15)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x+(w/2), (y+(h/2))))
        gameDisplay.blit(textSurf, textRect)

def game_intro():


    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(bright_blue)


        largeText = pygame.font.Font("freesansbold.ttf",60)
        TextSurf, TextRect = text_objects("CAR RACING", largeText)
        TextRect.center = ((display_width /2), (250))
        gameDisplay.blit(TextSurf, TextRect)

        carImg = pygame.image.load('racecar.png')
        gameDisplay.blit(carImg, (200, 500))
        carImg = pygame.image.load('racecar1.png')
        gameDisplay.blit(carImg, (500, 500))

        button("START",210,350,100,50,green,bright_green,'play')
        button("QUIT", 500,350,100, 50, red,bright_red,'quit')
        pygame.display.update()

        clock.tick(15)

def unpause():
    global pause
    pause=False


def paused():
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
        clock.tick(15)


def text_objects(text,font):
    textSurface=font.render(text,True,blue)
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

    largeText = pygame.font.SysFont("comicsansms", 50)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)

        button("Play Again", 150, 450, 100, 50, green, bright_green, 'play')
        button("Quit", 550, 450, 100, 50, red, bright_red, 'quit')

        pygame.display.update()
        clock.tick(15)
def game_loop():
    global pause
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

        gameDisplay.fill(black)

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

            thing_speed+=2
            thing_width+=1

        if y < thing_starty+thing_height:
            print('y crossed')

            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print('x crossed')
                crash()
        pygame.display.update()
        clock.tick(15)


game_intro()
game_loop()
pygame.quit()
quit()
