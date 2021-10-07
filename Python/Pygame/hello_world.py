#Date: 20-sep-2021

'''
    Description: este es nuestro primer script Python.
    Este script genera una ventana en Pygame con el título ¡Hello world!.
'''

#1. Importar librerias
import pygame
import sys

#2. Inicializar Pygame
pygame.init()

#3. Dimensionar (w x h) el tamaño de la ventana del video juego
#configuraciones generales de la ventana
width=800
height=400
mywindow = pygame.display.set_mode((width, height))
pygame.display.set_caption('Number race v 1.0')

#Cargar imagen
icon=pygame.image.load('images/controller.png')

#Setear imagen
pygame.display.set_icon(icon)

#Setear colores R(red) G(green) B(blue) => HxD
#RGB => 0-255
white=pygame.Color(255,255,255)
red=pygame.Color(255,0,0)
green=pygame.Color(0,255,0)
blue=pygame.Color(0,0,255)
x=pygame.Color(140,217,150)
y=pygame.Color(255,229,143)
bgColor=(100,100,100)
#Figures
#Rectangle:
rect1=pygame.Rect(150,300,150,50) #x,y,w,h
rect2=pygame.Rect(350,230,150,50)

rect1.center=(width//2,height//2)
#4. Mantener visible la ventana en pantalla
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: #valida si el usuario presiono cerrar ventana
            pygame.quit() #cierra la ventana
            sys.exit() #Cierra o destruye los procesos
    mywindow.fill(bgColor)
    pygame.draw.rect(mywindow,red,rect1) #ctx, color, rect
    pygame.draw.rect(mywindow,blue,rect2) #ctx, color, rect

    pygame.draw.rect(mywindow,green,(50,50,50,50))
    pygame.draw.line(mywindow,red,(10,10),(300,10),5)
    pygame.draw.circle(mywindow,y,(400,200),50)
    pygame.draw.polygon(mywindow,blue,((0,300),(100,200),(200,300)))
    pygame.display.update() #Actualizar