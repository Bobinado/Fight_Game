import pygame
from jugador import Personaje
pygame.init()

#Configuración de la ventana
alto=600
largo=800
screen=pygame.display.set_mode((largo,alto)) #PANTALLA
pygame.display.set_caption("No se que nombre poner todavia lol")
icon = pygame.image.load("icon.png").convert_alpha()
pygame.display.set_icon(icon)

#Configuración del fondo
fondo=pygame.image.load("fondos/fondo.png").convert_alpha()
def dibujar_fondo():
    screen.blit(fondo,(0,0))

#Cargar sprites de jugadores
jugador1_sheet = pygame.image.load("sprites_jugador/player_1.png")
jugador2_sheet = pygame.image.load("sprites_jugador/player_2.png")

#Número de pasos en cada animación
jugador1_pasos = [1, 12, 1, 3, 4]
jugador2_pasos = [1, 12, 1, 3, 4]

#variables del jugador
jugador1_tamaño = 64
jugador1_escala = 4
jugador1_offset = [20, 19]
jugador1_data = [jugador1_tamaño, jugador1_escala, jugador1_offset]

jugador2_tamaño = 64
jugador2_escala = 4
jugador2_offset = [20, 19]
jugador2_data = [jugador2_tamaño, jugador2_escala, jugador2_offset]


#Barras de vida
rojo = (255, 0, 0)
amarillo = (255, 255, 0)
blanco = (255, 255, 255)
def dibujar_vida(vida, x, y):
    relacion = vida / 100
    pygame.draw.rect(screen, rojo, (x, y, 350, 20))
    pygame.draw.rect(screen, amarillo, (x, y, 350 * relacion, 20)) #barra amarilla


#Jugadores
P1= Personaje(100, 150, False, jugador1_data, jugador1_sheet, jugador1_pasos)
P2= Personaje(600, 150, True, jugador2_data, jugador2_sheet, jugador2_pasos)

#Frame Rate
clock=pygame.time.Clock()
FPS=60


#BUCLE PRINCIPAL DEL JUEGO
run=True
while run: 
    clock.tick(FPS)

    dibujar_fondo()

    #dibujar barras
    dibujar_vida(P1.vida, 10, 10)
    dibujar_vida(P2.vida, 440, 10)

    #movimiento de personajes
    P1.mover(largo, alto, screen, P2)
    #P2.mover(largo, alto)
    
    #actualizar jugadores
    P1.actualizar()
    P2.actualizar()


    #dibujar jugadores
    P1.dibujar(screen)
    P2.dibujar(screen)


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        
        #P2.mover()
    pygame.display.update()