import pygame
from jugador import Personaje
pygame.init()

#CONFIGURACION DE LA VENTANA
alto=600
largo=800
screen=pygame.display.set_mode((largo,alto)) #PANTALLA
pygame.display.set_caption("Bruh")

#CONFIGURACIÓN DEL FONDO
fondo=pygame.image.load("fondos/fondo.png").convert_alpha()
def dibujar_fondo():
    screen.blit(fondo,(0,0))

#JUGADORES
P1= Personaje(150,200)
P2= Personaje(200,300)

#Frame Rate
clock=pygame.time.Clock()
FPS=60


#BUCLE PRINCIPAL DEL JUEGO
run=True
while run: 
    clock.tick(FPS)

    dibujar_fondo()
    P1.mover(largo, alto, screen, P2)
    #P2.mover(largo, alto)

    P1.dibujar(screen)
    P2.dibujar(screen)

    


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        
        #P2.mover()
    pygame.display.update()