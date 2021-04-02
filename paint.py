#!/usr/bin/env python3
import pygame
def song():
    file = "Prj/example.wav"
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)

pygame.init()
screen=pygame.display.set_mode([1200,600])
bgc=(255,255,255)
screen.fill(bgc)
pygame.display.set_caption("Python Paint")
keep_going=True
song()

#color()
WHITE=(255,255,255)
RED=(255,0,0)
YELLOW=(255,255,0)
GREEN=(102,204,0)
BLUE=(51,51,255)
BLACK=(0,0,0)
PINK=(255,0,255)

#menu
pygame.draw.rect(screen,RED,(0,50,20,20))
pygame.draw.rect(screen,YELLOW,(0,70,20,20))
pygame.draw.rect(screen,GREEN,(20,50,20,20))
pygame.draw.rect(screen,BLUE,(20,70,20,20))
pygame.draw.rect(screen,BLACK,(0,90,20,20))
pygame.draw.rect(screen,PINK,(20,90,20,20))
erasor = pygame.transform.scale(pygame.image.load("Prj/erasor.jpg"), (40, 40))
size1 = pygame.transform.scale(pygame.image.load("Prj/size1.png"), (40, 40))
size2=pygame.transform.scale(pygame.image.load("Prj/size2.png"),(40,40))
size3=pygame.transform.scale(pygame.image.load("Prj/size3.png"),(40,30))
screen.blit(erasor, [0,110])
screen.blit(size1, [0,150])
screen.blit(size2, [0,190])
screen.blit(size3, [0,230])

mousedn=False
color=BLACK
radius=9

#loop
while keep_going:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            keep_going=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            mousedn=True
            spot = pygame.mouse.get_pos()
            if spot[0] < 20 and spot[1] < 70 and spot[1] > 50:
                color= RED
            elif spot[0] < 40 and spot[0] > 20 and spot[1] < 70 and spot[1] > 50:
                color= GREEN
            elif spot[0] < 20 and spot[1] < 90 and spot[1] > 70:
                color= YELLOW
            elif spot[0] < 40 and spot[0] > 20 and spot[1] < 90 and spot[1] > 70:
                color= BLUE
            elif spot[0] < 20 and spot[1] < 110 and spot[1] > 90:
                color= BLACK
            elif spot[0] < 40 and spot[0] > 20 and spot[1] < 110 and spot[1] > 90:
                color= PINK
            elif spot[0] < 40 and spot[1] < 150 and spot[1] > 110:
                color = WHITE
            elif spot[0] < 40 and spot[1] < 190 and spot[1] > 150:
                radius=9
            elif spot[0] < 40 and spot[1] < 230 and spot[1] > 190:
                radius=5
            elif spot[0] < 40 and spot[1] < 260 and spot[1] > 230:
                radius=1

        if event.type==pygame.MOUSEBUTTONUP:
            mousedn=False
        if mousedn:
            spot = pygame.mouse.get_pos()
            if spot[0]>60:
                pygame.draw.circle(screen,color,spot,radius)
        #pygame.display.flip()
        pygame.display.update()
pygame.quit()

