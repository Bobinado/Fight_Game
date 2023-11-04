import pygame
from jugador import Personaje
pygame.init()

#CONFIGURACION DE LA VENTANA
alto=600
largo=800
screen=pygame.display.set_mode((largo,alto)) #PANTALLA
pygame.display.set_caption("nombre")

#CONFIGURACIÓN DEL FONDO
fondo=pygame.image.load("fondos/fondo.png").convert_alpha()
def dibujar_fondo():
    screen.blit(fondo,(0,0))

#BARRAS DE VIDA
rojo = (255, 0, 0)
amarillo = (255, 255, 0)
blanco = (255, 255, 255)
def dibujar_vida(vida, x, y):
    relacion = vida / 100
    pygame.draw.rect(screen, rojo, (x, y, 350, 20))
    pygame.draw.rect(screen, amarillo, (x, y, 350 * relacion, 20)) #barra amarilla


#Jugadores
P1= Personaje(100,150)
P2= Personaje(600,150)

#Frame Rate
clock=pygame.time.Clock()
FPS=60


#BUCLE PRINCIPAL DEL JUEGO
run=True
while run: 
    clock.tick(FPS)

    dibujar_fondo()

    dibujar_vida(P1.vida, 10, 10)
    dibujar_vida(P2.vida, 440, 10)

    P1.mover(largo, alto, screen, P2)
    #P2.mover(largo, alto)

    P1.dibujar(screen)
    P2.dibujar(screen)

    


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        
        #P2.mover()
    pygame.display.update()