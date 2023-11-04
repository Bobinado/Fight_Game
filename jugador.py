import pygame
class Personaje():
    
    #CREAR LOS PERSONAJES
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 100, 100))
        self.vel_y = 0
        self.salto = False
        self.tipo_ataque = 0
  
    #MOVIMIENTOS
    def mover(self, largo, alto, superficie, objetivo):
        velocidad = 10
        gravedad = 1
        dx = 0
        dy = 0
        key=pygame.key.get_pressed()

        #Movimiento
        if key[pygame.K_a]:
            dx=-velocidad
        if key[pygame.K_d]:
            dx=velocidad

        #Salto y gravedad
        if key[pygame.K_w] and self.salto==False:
            self.salto = True
            self.vel_y = -25
        
        self.vel_y += gravedad
        dy += self.vel_y

        #Ataques
        if key[pygame.K_c] or key[pygame.K_v]:
            self.atacar(superficie, objetivo)



        #Mantener al personaje dentro de la pantalla
        if self.rect.left + dx < 0:
            dx = -self.rect.left

        if self.rect.right + dx > largo:
            dx = largo - self.rect.right

        if self.rect.bottom + dy > alto-100:
            self.salto = False
            self.vel_y = 0
            dy = alto - 100 - self.rect.bottom

        self.rect.x+=dx
        self.rect.y+=dy

    def atacar(self, superficie, objetivo):
        atacante_rect = pygame.Rect(self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height)
        if atacante_rect.colliderect(objetivo.rect):
            print("golpe")
        
        
        pygame.draw.rect(superficie, (0,255,0), atacante_rect )

    #DIBUJAR LOS PERSONAJES
    def dibujar(self,superficie):
        pygame.draw.rect(superficie,(255,0,0), self.rect)
        
        

    