import pygame
import os
import random
pygame.init()

WINDOWW = 900
WINDOWH = 900
window = pygame.display.set_mode((WINDOWW,WINDOWH))
pygame.display.set_caption("DUMPLING MASTER")

FPS = 60
clock = pygame.time.Clock()

BUFFER = 100
BLACK = (0,0,0)
GREY = (107,107,107)
RED = (200,0,0)
WHITE = (200,200,200)
STARTINGLIVES = 10
STARTINGROCKVEL = 6
rockvel = STARTINGROCKVEL
lives = STARTINGLIVES
racoonvel = 10
score = 0


backgroundimage = pygame.image.load(os.path.join("assets","grass.png"))
backgroundrect = backgroundimage.get_rect()
backgroundrect.topleft = (0,0)
racoonimage = pygame.image.load(os.path.join("assets","racoon.png"))
racoonrect = racoonimage.get_rect()
racoonrect.center = (WINDOWW//2,WINDOWH//2)
smallrock2image = pygame.image.load(os.path.join("assets","smallrock2.png"))
smallrock2rect = smallrock2image.get_rect()
smallrock2rect.center = (100,0-BUFFER)
smallrock1image = pygame.image.load(os.path.join("assets","smallrock1.png"))
smallrock1rect = smallrock1image.get_rect()
smallrock1rect.center = (400,WINDOWH+BUFFER)
smallrock5image = pygame.image.load(os.path.join("assets","smallrock5.png"))
smallrock5rect = smallrock5image.get_rect()
smallrock5rect.center = (600,WINDOWH+BUFFER)
smallrock3image = pygame.image.load(os.path.join("assets","smallrock3.png"))
smallrock3rect = smallrock3image.get_rect()
smallrock3rect.center = (0-BUFFER,200)
smallrock4image = pygame.image.load(os.path.join("assets","smallrock4.png"))
smallrock4rect = smallrock4image.get_rect()
smallrock4rect.center = (WINDOWW+BUFFER,400)
dumpling1image = pygame.image.load(os.path.join("assets","dumpling1.png"))
dumpling1rect = dumpling1image.get_rect()
dumpling1rectx = random.randint(30, WINDOWW-30)
dumpling1recty = random.randint(30, WINDOWH-30)
dumpling1rect.center = (dumpling1rectx,dumpling1recty)
golddumplingimage = pygame.image.load(os.path.join("assets","golddumpling.png"))
golddumplingrect = golddumplingimage.get_rect()
golddumplingrectx = random.randint(30, WINDOWW-30)
golddumplingrecty = random.randint(30, WINDOWH-30)
golddumplingrect.center = (golddumplingrectx,golddumplingrecty)
dumpling2image = pygame.image.load(os.path.join("assets","dumpling2.png"))
dumpling2rect = dumpling2image.get_rect()
dumpling2rectx = random.randint(30, WINDOWW-30)
dumpling2recty = random.randint(30, WINDOWH-30)
dumpling2rect.center = (dumpling2rectx,dumpling2recty)
dumpling3image = pygame.image.load(os.path.join("assets","dumpling3.png"))
dumpling3rect = dumpling3image.get_rect()
dumpling3rectx = random.randint(30, WINDOWW-30)
dumpling3recty = random.randint(30, WINDOWH-30)
dumpling3rect.center = (dumpling3rectx,dumpling3recty)
dumpling4image = pygame.image.load(os.path.join("assets","dumpling4.png"))
dumpling4rect = dumpling4image.get_rect()
dumpling4rectx = random.randint(30, WINDOWW-30)
dumpling4recty = random.randint(30, WINDOWH-30)
dumpling4rect.center = (dumpling4rectx,dumpling4recty)

eatsound = pygame.mixer.Sound(os.path.join("assets","eat.mp3"))
hurtsound = pygame.mixer.Sound(os.path.join("assets","hurt.mp3"))
gameoversound = pygame.mixer.Sound(os.path.join("assets","gameover.mp3"))
boostsound = pygame.mixer.Sound(os.path.join("assets","boost.mp3"))
pygame.mixer.music.load(os.path.join("assets","background.mp3"))

font = pygame.font.Font(os.path.join("assets", "font.ttf"), 32)
scoretext = font.render("Score: "+str(score), True, WHITE, GREY)
scorerect = scoretext.get_rect()
scorerect.topleft = (10,10)
livestext = font.render("Lives: "+str(lives), True, WHITE, GREY)
livesrect = livestext.get_rect()
livesrect.topright = (WINDOWW-10, 10)
titletext = font.render("The Dumpling Master", True, WHITE, GREY)
titlerect = titletext.get_rect()
titlerect.center = (WINDOWW//2,26)
gameovertext = font.render("you died!", True, WHITE,GREY)
gameoverrect = gameovertext.get_rect()
gameoverrect.center = (WINDOWW//2,WINDOWH//2-16)
continuetext = font.render("press any key to play again",True, WHITE, GREY)
continuerect = continuetext.get_rect()
continuerect.center = (WINDOWW//2,WINDOWH//2+16)

smallrock2direction = None
if smallrock2rect.y > WINDOWH:
    smallrock2direction = "up"
elif smallrock2rect.y < 0:
    smallrock2direction = "down"
elif smallrock2rect.x > WINDOWW:
    smallrock2direction = "left"
elif smallrock2rect.x < 0:
    smallrock2direction = "right"
def resetsmallrock2():
    global smallrock2direction
    global smallrock2rect
    xory = random.choice(["x","y"])
    if xory == "x":
        smallrock2rect.x = random.choice([WINDOWW+BUFFER,0-BUFFER])
        smallrock2rect.y = random.randint(0+24,WINDOWH-24)
    if xory == "y":
        smallrock2rect.x = random.randint(0+24,WINDOWW-24)
        smallrock2rect.y = random.choice([WINDOWH+BUFFER,0-BUFFER])
    if smallrock2rect.y > WINDOWH:
        smallrock2direction = "up"
    elif smallrock2rect.y < 0:
        smallrock2direction = "down"
    elif smallrock2rect.x > WINDOWW:
        smallrock2direction = "left"
    elif smallrock2rect.x < 0:
        smallrock2direction = "right"

smallrock4direction = None
if smallrock4rect.y > WINDOWH:
    smallrock4direction = "up"
elif smallrock4rect.y < 0:
    smallrock4direction = "down"
elif smallrock4rect.x > WINDOWW:
    smallrock4direction = "left"
elif smallrock4rect.x < 0:
    smallrock4direction = "right"
def resetsmallrock4():
    global smallrock4direction
    global smallrock4rect
    xory = random.choice(["x","y"])
    if xory == "x":
        smallrock4rect.x = random.choice([WINDOWW+BUFFER,0-BUFFER])
        smallrock4rect.y = random.randint(0+24,WINDOWH-24)
    if xory == "y":
        smallrock4rect.x = random.randint(0+24,WINDOWW-24)
        smallrock4rect.y = random.choice([WINDOWH+BUFFER,0-BUFFER])
    if smallrock4rect.y > WINDOWH:
        smallrock4direction = "up"
    elif smallrock4rect.y < 0:
        smallrock4direction = "down"
    elif smallrock4rect.x > WINDOWW:
        smallrock4direction = "left"
    elif smallrock4rect.x < 0:
        smallrock4direction = "right"


smallrock1direction = None
if smallrock1rect.y > WINDOWH:
    smallrock1direction = "up"
elif smallrock1rect.y < 0:
    smallrock1direction = "down"
elif smallrock1rect.x > WINDOWW:
    smallrock1direction = "left"
elif smallrock1rect.x < 0:
    smallrock1direction = "right"
def resetsmallrock1():
    global smallrock1direction
    global smallrock1rect
    xory = random.choice(["x","y"])
    if xory == "x":
        smallrock1rect.x = random.choice([WINDOWW+BUFFER,0-BUFFER])
        smallrock1rect.y = random.randint(0+24,WINDOWH-24)
    if xory == "y":
        smallrock1rect.x = random.randint(0+24,WINDOWW-24)
        smallrock1rect.y = random.choice([WINDOWH+BUFFER,0-BUFFER])
    if smallrock1rect.y > WINDOWH:
        smallrock1direction = "up"
    elif smallrock1rect.y < 0:
        smallrock1direction = "down"
    elif smallrock1rect.x > WINDOWW:
        smallrock1direction = "left"
    elif smallrock1rect.x < 0:
        smallrock1direction = "right"

smallrock3direction = None
if smallrock3rect.y > WINDOWH:
    smallrock3direction = "up"
elif smallrock3rect.y < 0:
    smallrock3direction = "down"
elif smallrock3rect.x > WINDOWW:
    smallrock3direction = "left"
elif smallrock3rect.x < 0:
    smallrock3direction = "right"
def resetsmallrock3():
    global smallrock3direction
    global smallrock3rect
    xory = random.choice(["x","y"])
    if xory == "x":
        smallrock3rect.x = random.choice([WINDOWW+BUFFER,0-BUFFER])
        smallrock3rect.y = random.randint(0+24,WINDOWH-24)
    if xory == "y":
        smallrock3rect.x = random.randint(0+24,WINDOWW-24)
        smallrock3rect.y = random.choice([WINDOWH+BUFFER,0-BUFFER])
    if smallrock3rect.y > WINDOWH:
        smallrock3direction = "up"
    elif smallrock3rect.y < 0:
        smallrock3direction = "down"
    elif smallrock3rect.x > WINDOWW:
        smallrock3direction = "left"
    elif smallrock3rect.x < 0:
        smallrock3direction = "right"

smallrock5direction = None
if smallrock5rect.y > WINDOWH:
    smallrock5direction = "up"
elif smallrock5rect.y < 0:
    smallrock5direction = "down"
elif smallrock5rect.x > WINDOWW:
    smallrock5direction = "left"
elif smallrock5rect.x < 0:
    smallrock5direction = "right"
def resetsmallrock5():
    global smallrock5direction
    global smallrock5rect
    xory = random.choice(["x","y"])
    if xory == "x":
        smallrock5rect.x = random.choice([WINDOWW+BUFFER,0-BUFFER])
        smallrock5rect.y = random.randint(0+24,WINDOWH-24)
    if xory == "y":
        smallrock5rect.x = random.randint(0+24,WINDOWW-24)
        smallrock5rect.y = random.choice([WINDOWH+BUFFER,0-BUFFER])
    if smallrock5rect.y > WINDOWH:
        smallrock5direction = "up"
    elif smallrock5rect.y < 0:
        smallrock5direction = "down"
    elif smallrock5rect.x > WINDOWW:
        smallrock5direction = "left"
    elif smallrock5rect.x < 0:
        smallrock5direction = "right"

running = True
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(0.5)
currenttime = 0
golddumplingtimer = 0
golddumplingtimer1 = 0
smallrocktimer = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    currenttime = pygame.time.get_ticks()   
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and racoonrect.top > 0:
        racoonrect.y -= racoonvel
    if keys[pygame.K_s] and racoonrect.bottom < WINDOWH:
        racoonrect.y += racoonvel
    if keys[pygame.K_a] and racoonrect.left > 0:
        racoonrect.x -= racoonvel
    if keys[pygame.K_d] and racoonrect.right  <WINDOWW:
        racoonrect.x += racoonvel

    if racoonrect.colliderect(dumpling1rect):
        score+=1
        eatsound.play()
        dumpling1rect.x = random.randint(30, WINDOWW-30)
        dumpling1rect.y = random.randint(30, WINDOWH-30)
    if racoonrect.colliderect(dumpling2rect):
        score+=1
        eatsound.play()
        dumpling2rect.x = random.randint(30, WINDOWW-30)
        dumpling2rect.y = random.randint(30, WINDOWH-30)
    if racoonrect.colliderect(dumpling3rect):
        score+=1
        eatsound.play()
        dumpling3rect.x = random.randint(30, WINDOWW-30)
        dumpling3rect.y = random.randint(30, WINDOWH-30)
    if racoonrect.colliderect(dumpling4rect):
        score+=1
        eatsound.play()
        dumpling4rect.x = random.randint(30, WINDOWW-30)
        dumpling4rect.y = random.randint(30, WINDOWH-30)
    if racoonrect.colliderect(golddumplingrect):
        score+=1
        lives+=1
        eatsound.play()
        boostsound.play()
        racoonvel = racoonvel * 1.5
        golddumplingrect.x = WINDOWW+BUFFER
        golddumplingrect.y = WINDOWH+BUFFER
        golddumplingtimer = pygame.time.get_ticks()
    if golddumplingtimer > 0 and currenttime - golddumplingtimer > 5000:
        racoonvel = racoonvel/1.5
        golddumplingtimer = 0
        golddumplingtimer1 = pygame.time.get_ticks()
    if golddumplingtimer1 > 0 and currenttime - golddumplingtimer1 > 5000:
        golddumplingrect.x = random.randint(30, WINDOWW-30)
        golddumplingrect.y = random.randint(30, WINDOWH-30)
        golddumplingtimer1 = 0
    if racoonrect.colliderect(smallrock1rect):
        xory = random.choice(["x","y"])
        if xory == "x":
            smallrock1rect.x = random.choice([WINDOWW+BUFFER,0-BUFFER])
            smallrock1rect.y = random.randint(0,WINDOWH)
        if xory == "y":
            smallrock1rect.x = random.randint(0,WINDOWW)
            smallrock1rect.y = random.choice([WINDOWH+BUFFER,0-BUFFER])
        lives -= 1
        hurtsound.play()
        racoonrect.center = (WINDOWW//2,WINDOWH//2)
    if racoonrect.colliderect(smallrock2rect):
        xory = random.choice(["x","y"])
        if xory == "x":
            smallrock2rect.x = random.choice([WINDOWW+BUFFER,0-BUFFER])
            smallrock2rect.y = random.randint(0,WINDOWH)
        if xory == "y":
            smallrock2rect.x = random.randint(0,WINDOWW)
            smallrock2rect.y = random.choice([WINDOWH+BUFFER,0-BUFFER])
        lives -= 1
        hurtsound.play()
        racoonrect.center = (WINDOWW//2,WINDOWH//2)
    if racoonrect.colliderect(smallrock3rect):
        xory = random.choice(["x","y"])
        if xory == "x":
            smallrock3rect.x = random.choice([WINDOWW+BUFFER,0-BUFFER])
            smallrock3rect.y = random.randint(0,WINDOWH)
        if xory == "y":
            smallrock3rect.x = random.randint(0,WINDOWW)
            smallrock3rect.y = random.choice([WINDOWH+BUFFER,0-BUFFER])
        lives -= 1
        hurtsound.play()
        racoonrect.center = (WINDOWW//2,WINDOWH//2)
    if racoonrect.colliderect(smallrock4rect):
        xory = random.choice(["x","y"])
        if xory == "x":
            smallrock4rect.x = random.choice([WINDOWW+BUFFER,0-BUFFER])
            smallrock4rect.y = random.randint(0,WINDOWH)
        if xory == "y":
            smallrock4rect.x = random.randint(0,WINDOWW)
            smallrock4rect.y = random.choice([WINDOWH+BUFFER,0-BUFFER])
        lives -= 1
        hurtsound.play()
        racoonrect.center = (WINDOWW//2,WINDOWH//2)
    if racoonrect.colliderect(smallrock5rect):
        xory = random.choice(["x","y"])
        if xory == "x":
            smallrock5rect.x = random.choice([WINDOWW+BUFFER,0-BUFFER])
            smallrock5rect.y = random.randint(0,WINDOWH)
        if xory == "y":
            smallrock5rect.x = random.randint(0,WINDOWW)
            smallrock5rect.y = random.choice([WINDOWH+BUFFER,0-BUFFER])
        lives -= 1
        hurtsound.play()
        racoonrect.center = (WINDOWW//2,WINDOWH//2)

    if score >5:
        if smallrock2direction == "left":
            if smallrock2rect.x > 0:
                smallrock2rect.x -= rockvel
            if smallrock2rect.x < 0:
                resetsmallrock2()
        if smallrock2direction == "right":
            if smallrock2rect.x < WINDOWW:
                smallrock2rect.x += rockvel
            if smallrock2rect.x > WINDOWW:
                resetsmallrock2()
        if smallrock2direction == "up":
            if smallrock2rect.y > 0:
                smallrock2rect.y -= rockvel
            if smallrock2rect.y <0:
                resetsmallrock2()
        if smallrock2direction == "down":
            if smallrock2rect.y < WINDOWH:
                smallrock2rect.y += rockvel
            if smallrock2rect.y > WINDOWH:
                resetsmallrock2()

    if score> 10:
        if smallrock4direction == "left":
            if smallrock4rect.x > 0:
                smallrock4rect.x -= rockvel
            if smallrock4rect.x < 0:
                resetsmallrock4()
        if smallrock4direction == "right":
            if smallrock4rect.x < WINDOWW:
                smallrock4rect.x += rockvel
            if smallrock4rect.x > WINDOWW:
                resetsmallrock4()
        if smallrock4direction == "up":
            if smallrock4rect.y > 0:
                smallrock4rect.y -= rockvel
            if smallrock4rect.y <0:
                resetsmallrock4()
        if smallrock4direction == "down":
            if smallrock4rect.y < WINDOWH:
                smallrock4rect.y += rockvel
            if smallrock4rect.y > WINDOWH:
                resetsmallrock4()

    if score > 15:
        if smallrock3direction == "left":
            if smallrock3rect.x > 0:
                smallrock3rect.x -= rockvel
            if smallrock3rect.x < 0:
                resetsmallrock3()
        if smallrock3direction == "right":
            if smallrock3rect.x < WINDOWW:
                smallrock3rect.x += rockvel
            if smallrock3rect.x > WINDOWW:
                resetsmallrock3()
        if smallrock3direction == "up":
            if smallrock3rect.y > 0:
                smallrock3rect.y -= rockvel
            if smallrock3rect.y <0:
                resetsmallrock3()
        if smallrock3direction == "down":
            if smallrock3rect.y < WINDOWH:
                smallrock3rect.y += rockvel
            if smallrock3rect.y > WINDOWH:
                resetsmallrock3()

    if score > 20:
        if smallrock1direction == "left":
            if smallrock1rect.x > 0:
                smallrock1rect.x -= rockvel
            if smallrock1rect.x < 0:
                resetsmallrock1()
        if smallrock1direction == "right":
            if smallrock1rect.x < WINDOWW:
                smallrock1rect.x += rockvel
            if smallrock1rect.x > WINDOWW:
                resetsmallrock1()
        if smallrock1direction == "up":
            if smallrock1rect.y > 0:
                smallrock1rect.y -= rockvel
            if smallrock1rect.y <0:
                resetsmallrock1()
        if smallrock1direction == "down":
            if smallrock1rect.y < WINDOWH:
                smallrock1rect.y += rockvel
            if smallrock1rect.y > WINDOWH:
                resetsmallrock1()

    if smallrock5direction == "left":
        if smallrock5rect.x > 0:
            smallrock5rect.x -= rockvel
        if smallrock5rect.x < 0:
            resetsmallrock5()
    if smallrock5direction == "right":
        if smallrock5rect.x < WINDOWW:
            smallrock5rect.x += rockvel
        if smallrock5rect.x > WINDOWW:
            resetsmallrock5()
    if smallrock5direction == "up":
        if smallrock5rect.y > 0:
            smallrock5rect.y -= rockvel
        if smallrock5rect.y <0:
            resetsmallrock5()
    if smallrock5direction == "down":
        if smallrock5rect.y < WINDOWH:
            smallrock5rect.y += rockvel
        if smallrock5rect.y > WINDOWH:
            resetsmallrock5()

    if lives <= 0:
        gameoversound.play()
        paused = True
        pygame.mixer.music.stop()
        while paused:
            window.blit(gameovertext,gameoverrect)
            window.blit(continuetext,continuerect)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    paused = False
                    running = False
                if event.type == pygame.KEYDOWN:
                    pygame.mixer.music.play(-1,0.0)
                    lives = STARTINGLIVES
                    racoonrect.center = (WINDOWW//2,WINDOWH//2)
                    score = 0
                    rockvel = STARTINGROCKVEL
                    smallrock2rect.center = (100,0-BUFFER)
                    smallrock5rect.center = (600,WINDOWH+BUFFER)
                    smallrock4rect.center = (WINDOWW+BUFFER,400)
                    smallrock1rect.center = (400,WINDOWH+BUFFER)
                    smallrock3rect.center = (0-BUFFER,200)
                    paused = False


    if score >= 3 and score < 50:
        rockvel = 9
    if score >= 50 and score < 70:
        rockvel = 12
    if score >= 70 and score < 90:
        rockvel = 15
    if score >= 90 and score < 110:
        rockvel = 18
    if score >= 110 and score < 130:
        rockvel = 21
    if score >= 130 and score < 150:
        rockvel = 24
    if score >= 150 and score < 170:
        rockvel = 27
    if score >= 170 and score < 190:
        rockvel = 30
    if score >= 190:
        rockvel = 33



    scoretext = font.render("Score: "+str(score), True, WHITE, GREY)
    livestext = font.render("Lives: "+str(lives), True, WHITE, GREY)

    window.blit(backgroundimage,backgroundrect)
    window.blit(scoretext,scorerect)
    window.blit(livestext,livesrect)
    window.blit(titletext,titlerect)
    window.blit(smallrock1image,smallrock1rect)
    window.blit(smallrock2image,smallrock2rect)
    window.blit(smallrock3image,smallrock3rect)
    window.blit(smallrock4image,smallrock4rect)
    window.blit(smallrock5image,smallrock5rect)
    window.blit(golddumplingimage,golddumplingrect) 
    window.blit(dumpling1image,dumpling1rect)
    window.blit(dumpling2image,dumpling2rect)
    window.blit(dumpling3image,dumpling3rect)
    window.blit(dumpling4image,dumpling4rect)
    window.blit(racoonimage,racoonrect)

    clock.tick(60)
    pygame.display.update()

pygame.quit()