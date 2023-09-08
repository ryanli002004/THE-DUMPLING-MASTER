import pygame
import os
import time
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
lives = STARTINGLIVES
racoonvel = 10
score = 0

racoonimage = pygame.image.load(os.path.join("assets","racoon.png"))
racoonrect = racoonimage.get_rect()
racoonrect.center = (WINDOWW//2,WINDOWH//2)
bearimage = pygame.image.load(os.path.join("assets","bear.png"))
bearrect = bearimage.get_rect()
bearrect.center = (100,100)
lionimage = pygame.image.load(os.path.join("assets","lion.png"))
lionrect = lionimage.get_rect()
lionrect.center = (200,100)
smallrock2image = pygame.image.load(os.path.join("assets","smallrock2.png"))
smallrock2rect = smallrock2image.get_rect()
smallrock2rect.center = (300,100)
smallrock1image = pygame.image.load(os.path.join("assets","smallrock1.png"))
smallrock1rect = smallrock1image.get_rect()
smallrock1rect.center = (400,100)
bigrockimage = pygame.image.load(os.path.join("assets","bigrock.png"))
bigrockrect = bigrockimage.get_rect()
bigrockrect.center = (500,100)
uplaserimage = pygame.image.load(os.path.join("assets","uplaser.png"))
uplaserrect = uplaserimage.get_rect()
uplaserrect.center = (600,100)
downlaserimage = pygame.image.load(os.path.join("assets","downlaser.png"))
downlaserrect = downlaserimage.get_rect()
downlaserrect.center = (700,100)
rightlaserimage = pygame.image.load(os.path.join("assets","rightlaser.png"))
rightlaserrect = rightlaserimage.get_rect()
rightlaserrect.center = (100,200)
leftlaserimage = pygame.image.load(os.path.join("assets","leftlaser.png"))
leftlaserrect = leftlaserimage.get_rect()
leftlaserrect.center = (200,200)
wolfimage = pygame.image.load(os.path.join("assets","wolf.png"))
wolfrect = wolfimage.get_rect()
wolfrect.center = (300,200)
crocimage = pygame.image.load(os.path.join("assets","croc.png"))
crocrect = crocimage.get_rect()
crocrect.center = (400,200)
bigrock2image = pygame.image.load(os.path.join("assets","bigrock2.png"))
bigrock2rect = bigrock2image.get_rect()
bigrock2rect.center = (500,200)
smallrock3image = pygame.image.load(os.path.join("assets","smallrock3.png"))
smallrock3rect = smallrock3image.get_rect()
smallrock3rect.center = (600,200)
smallrock4image = pygame.image.load(os.path.join("assets","smallrock4.png"))
smallrock4rect = smallrock4image.get_rect()
smallrock4rect.center = (700,200)
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

eatsound = pygame.mixer.Sound()

font = pygame.font.Font(os.path.join("assets", "font.ttf"), 32)
scoretext = font.render("Score: "+str(score), True, WHITE, GREY)
scorerect = scoretext.get_rect()
scorerect.topleft = (10,10)
livestext = font.render("Lives: "+str(lives), True, WHITE, GREY)
livesrect = livestext.get_rect()
livesrect.topleft = (10, 52)
gameovertext = font.render("you died!", True, WHITE,GREY)
gameoverrect = gameovertext.get_rect()
gameoverrect.center = (WINDOWW//2,WINDOWH//2-16)
continuetext = font.render("press any key to play again",True, WHITE, GREY)
continuerect = continuetext.get_rect()
continuerect.center = (WINDOWW//2,WINDOWH//2+16)


running = True
currenttime = 0
golddumplingtimer = 0
golddumplingtimer1 = 0
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
        dumpling1rect.x = random.randint(30, WINDOWW-30)
        dumpling1rect.y = random.randint(30, WINDOWH-30)
    if racoonrect.colliderect(dumpling2rect):
        score+=1
        dumpling2rect.x = random.randint(30, WINDOWW-30)
        dumpling2rect.y = random.randint(30, WINDOWH-30)
    if racoonrect.colliderect(dumpling3rect):
        score+=1
        dumpling3rect.x = random.randint(30, WINDOWW-30)
        dumpling3rect.y = random.randint(30, WINDOWH-30)
    if racoonrect.colliderect(dumpling4rect):
        score+=1
        dumpling4rect.x = random.randint(30, WINDOWW-30)
        dumpling4rect.y = random.randint(30, WINDOWH-30)
    if racoonrect.colliderect(golddumplingrect):
        score+=1
        lives+=1
        racoonvel = racoonvel * 2
        golddumplingrect.x = WINDOWW+BUFFER
        golddumplingrect.y = WINDOWH+BUFFER
        golddumplingtimer = pygame.time.get_ticks()
    if golddumplingtimer > 0 and currenttime - golddumplingtimer > 3000:
        racoonvel = racoonvel/2
        golddumplingtimer = 0
        golddumplingtimer1 = pygame.time.get_ticks()
    if golddumplingtimer1 > 0 and currenttime - golddumplingtimer1 > 4000:
        golddumplingrect.x = random.randint(30, WINDOWW-30)
        golddumplingrect.y = random.randint(30, WINDOWH-30)
        golddumplingtimer1 = 0
    if racoonrect.colliderect(leftlaserrect):
        lives -= 1
        racoonrect.center = (WINDOWW//2,WINDOWH//2)
    if racoonrect.colliderect(rightlaserrect):
        lives -= 1
        racoonrect.center = (WINDOWW//2,WINDOWH//2) 
    if racoonrect.colliderect(uplaserrect):
        lives -= 1
        racoonrect.center = (WINDOWW//2,WINDOWH//2)
    if racoonrect.colliderect(downlaserrect):
        lives -= 1
        racoonrect.center = (WINDOWW//2,WINDOWH//2)
    if racoonrect.colliderect(bearrect):
        lives -= 1
        racoonrect.center = (WINDOWW//2,WINDOWH//2)
    if racoonrect.colliderect(lionrect):
        lives -= 1
        racoonrect.center = (WINDOWW//2,WINDOWH//2)
    if racoonrect.colliderect(bigrockrect):
        lives -= 1
        racoonrect.center = (WINDOWW//2,WINDOWH//2)
    if racoonrect.colliderect(smallrock1rect):
        lives -= 1
        racoonrect.center = (WINDOWW//2,WINDOWH//2)
    if racoonrect.colliderect(smallrock2rect):
        lives -= 1
        racoonrect.center = (WINDOWW//2,WINDOWH//2)
    if racoonrect.colliderect(smallrock3rect):
        lives -= 1
        racoonrect.center = (WINDOWW//2,WINDOWH//2)
    if racoonrect.colliderect(smallrock4rect):
        lives -= 1
        racoonrect.center = (WINDOWW//2,WINDOWH//2)
    if racoonrect.colliderect(bigrock2rect):
        lives -= 1
        racoonrect.center = (WINDOWW//2,WINDOWH//2)
    if racoonrect.colliderect(wolfrect):
        lives -= 1
        racoonrect.center = (WINDOWW//2,WINDOWH//2)
    if racoonrect.colliderect(crocrect):
        lives -= 1
        racoonrect.center = (WINDOWW//2,WINDOWH//2)

    if lives <= 0:
        paused = True
        while paused:
            window.blit(gameovertext,gameoverrect)
            window.blit(continuetext,continuerect)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    paused = False
                    running = False
                if event.type == pygame.KEYDOWN:
                    lives = STARTINGLIVES
                    racoonrect.center = (WINDOWW//2,WINDOWH//2)
                    score = 0
                    paused = False


    scoretext = font.render("Score: "+str(score), True, WHITE, GREY)
    livestext = font.render("Lives: "+str(lives), True, WHITE, GREY)

    window.fill(BLACK)
    window.blit(scoretext,scorerect)
    window.blit(livestext,livesrect)
    window.blit(smallrock1image,smallrock1rect)
    window.blit(smallrock2image,smallrock2rect)
    window.blit(bearimage,bearrect)
    window.blit(lionimage,lionrect)
    window.blit(bigrockimage,bigrockrect)
    window.blit(leftlaserimage,leftlaserrect)
    window.blit(rightlaserimage,rightlaserrect)
    window.blit(uplaserimage,uplaserrect)
    window.blit(downlaserimage,downlaserrect)
    window.blit(bigrock2image,bigrock2rect)
    window.blit(smallrock3image,smallrock3rect)
    window.blit(smallrock4image,smallrock4rect)
    window.blit(wolfimage,wolfrect)
    window.blit(lionimage,lionrect)
    window.blit(crocimage,crocrect)
    window.blit(golddumplingimage,golddumplingrect)
    window.blit(dumpling1image,dumpling1rect)
    window.blit(dumpling2image,dumpling2rect)
    window.blit(dumpling3image,dumpling3rect)
    window.blit(dumpling4image,dumpling4rect)
    window.blit(racoonimage,racoonrect)

    clock.tick(60)
    pygame.display.update()

pygame.quit()