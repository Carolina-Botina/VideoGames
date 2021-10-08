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
        #A mayor amplitud rebote afecta eje Y y a menor amplitud rebote afect eje X
        self.speed=[5,5] #[Param1->Veloc del mov. /Param2 -> Amplitud del mov. ] -> Concepto de las físicas

    def pibot(self):
        #Validate Y !¡
        if self.rect.bottom >= HEIGHT or self.rect.top <=0:
            self.speed[1] = -self.speed[1]
        #Validate x <- X ->
        elif self.rect.right >= WIDTH or self.rect.left <=0:
            self.speed[0] = -self.speed[0]

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
        if listener.key == pygame.K_LEFT and self.rect.left > 0:
            self.speed=[-5,0]
        elif listener.key == pygame.K_RIGHT and self.rect.right < WIDTH:
            self.speed = [5,0]
        else:
            self.speed=[0,0]
        self.rect.move_ip(self.speed)
##################################################################
class Brick(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('images/ladrillo.png')
        self.rect=self.image.get_rect()
        self.rect.topleft=position

class Wall(pygame.sprite.Group):
    def __init__(self,totalBricks):
        pygame.sprite.Group.__init__(self)
        posX=0
        posY=10

        for i in range(totalBricks):
            brick=Brick((posX,posY))
            self.add(brick)

            posX+=brick.rect.width
            if posX >= WIDTH:
                posX=0
                posY+=brick.rect.height
#######################################################

#General settings
WIDTH=640
HEIGHT=480
BG_COLOR=(52,102,95) #(R,G,B)

screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Atari')
icon=pygame.image.load('images/controller.png')
pygame.display.set_icon(icon)

game_clock=pygame.time.Clock()  #Reloj del juego
pygame.key.set_repeat(20)
ball=Ball()
player=Bar()

totalBricks = int(input("Digite la cantidad de ladrillos:"))

wall=Wall(totalBricks)

#Loop (Revisión cíclica de los eventos) => Listener
while True:
    game_clock.tick(60)
    for event in pygame.event.get():
        #Verificar si se presiono el botón X de la ventana
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Verificar si el jugador presionó tecla del teclado
        elif event.type==pygame.KEYDOWN:
            player.slide(event)
    #Call pibot
    ball.pibot()

    #Collision between bar and ball
    #Cambio de trayectoria de la bola
    if pygame.sprite.collide_rect(ball,player): #PLayer is the bar
        ball.speed[1] = -ball.speed[1]

    #Collision between ball and wall (Bricks) Destroy bricks
    elements = pygame.sprite.spritecollide(ball,wall,False,collided=None)
    if elements: #Mientras existan ladrillos para chocar
        brick = elements[0]
        centX = ball.rect.centerx

        if centX < brick.rect.left or centX > brick.rect.right:
            #Afectamos velocidad
            ball.speed[0] = -ball.speed[0]
        else:
            #Afectamos trayectoria
            ball.speed[1] = -ball.speed[1]
        wall.remove(brick)





    #Set background color
    screen.fill(BG_COLOR)
    #Draw de la ball
    screen.blit(ball.img_ball,ball.rect)
    #Draw de la bar
    screen.blit(player.img_bar,player.rect)
    #Draw wall
    wall.draw(screen)
    pygame.display.flip() #Refresh de elementos en screen