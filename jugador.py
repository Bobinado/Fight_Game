import pygame
class Personaje():
    
    #CREAR LOS PERSONAJES
    def __init__(jugador, self, x, y):
        self.jugador = jugador
        self.direccion = False
        self.rect = pygame.Rect((x, y, 100, 100))
        self.vel_y = 0
        self.salto = False
        self.atacando = False
        self.tipo_ataque = 0
        self.vida = 100
  
    #MOVIMIENTOS
    def mover(self, largo, alto, superficie, objetivo):
        velocidad = 10
        gravedad = 1
        dx = 0
        dy = 0
        key=pygame.key.get_pressed()

        
        if self.atacando == False: #Solo moverse si no está atacando
            if jugador == 1:

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
                    if key[pygame.K_c]:
                        self.tipo_ataque = 1
                    if key[pygame.K_v]:
                        self.tipo_ataque = 2

            if jugador == 2:

                #Movimiento
                if key[pygame.K_LEFT]:
                    dx=-velocidad
                if key[pygame.K_RIGHT]:
                    dx=velocidad

                #Salto y gravedad
                if key[pygame.K_UP] and self.salto==False:
                    self.salto = True
                    self.vel_y = -25
                
                self.vel_y += gravedad
                dy += self.vel_y

                #Ataques
                if key[pygame.K_o] or key[pygame.K_p]:
                    self.atacar(superficie, objetivo)
                    if key[pygame.K_c]:
                        self.tipo_ataque = 1
                    if key[pygame.K_v]:
                        self.tipo_ataque = 2



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

        #Mantener a los personajes opuestos entre sí
        if objetivo.rect.centerx > self.rect.centerx:
            self.direccion = False
        else: 
            self.direccion = True


    def atacar(self, superficie, objetivo):
        self.atacando = True
        atacante_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.direccion) , self.rect.y, 2 * self.rect.width, self.rect.height)
        if atacante_rect.colliderect(objetivo.rect):
            objetivo.vida -=5
        
        
        
        pygame.draw.rect(superficie, (0, 255, 0), atacante_rect )

    #DIBUJAR LOS PERSONAJES
    def dibujar(self,superficie):
        pygame.draw.rect(superficie,(255, 0, 0), self.rect)
        
        

    