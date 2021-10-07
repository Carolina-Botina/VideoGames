'''
    Developer: Carolina Botina
    Date: 30-sept-2021
    Description: Desarrollo de la versión 1.0 de un video juego de atari.
'''

#Importar librerias
import pygame
import sys

pygame.init()
#############################
#Classes
#############################
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img_ball=pygame.image.load('images/bolita.png')
        self.rect=self.img_ball.get_rect()
        self.rect.centerx=WIDTH / 2
        self.rect.centery=HEIGHT / 2
        self.speed=[1,1] #[]

    def pibot(self):
        #Validate Y!¡
        if self.rect.bottom >= HEIGHT or self.rect.top <=0:
            self.speed[1] = -self.speed[1]

        self.rect.move_ip(self.speed)

##############################################################################
class Bar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img_bar=pygame.image.load('images/paleta.png')
        self.rect=self.img_bar.get_rect()
        self.rect.midbottom=(WIDTH/2,HEIGHT-10)
        self.speed=[0,0]

    def slide(self,listener):
        if listener.key == pygame.K_LEFT and self.rect.left >0:
            self.speed=[-3,0]
        elif listener.key == pygame.K_RIGHT and self.right>WIDTH:
            self.speed = [3,0]
#General settings
WIDTH=640
HEIGHT=480
BG_COLOR=(52,102,95) #(R,G,B)

screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Atari')
icon=pygame.image.load('images/controller.png')
pygame.display.set_icon(icon)

game_clock=pygame.time.Clock() #Reloj del juego
ball=Ball()
player=Bar()

#Loop (Revisión cíclica de los eventos) => Listener
while True:
    game_clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Set ball pibot
    ball.pibot()
    #Set background color
    screen.fill(BG_COLOR)
    #Draw de la ball
    screen.blit(ball.img_ball,ball.rect)
    #Draw de la bar
    screen.blit(player.img_bar,player.rect)
    pygame.display.flip() #Refresh de elementos en screen