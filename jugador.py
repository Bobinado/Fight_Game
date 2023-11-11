import pygame
class Personaje():
    
    #CREAR LOS PERSONAJES
    def __init__(self, jugador, x, y, direccion, data, hoja_sprites, pasos_animacion):
        self.jugador = jugador
        self.tamaño = data[0]
        self.escala_imagen = data[1]
        self.offset = data[2]
        self.direccion = direccion
        self.lista_animacion = self.cargar_imagenes(hoja_sprites, pasos_animacion)
        self.accion = 0 #0:idle 1:atacar 2:saltar 3:correr 4: muerte: 5:daño
        self.frame_index = 0
        self.imagen = self.lista_animacion[self.accion][self.frame_index]
        self.actualizacion = pygame.time.get_ticks()
        self.rect = pygame.Rect((x, y, 100, 125))
        self.vel_y = 0
        self.corriendo = False
        self.salto = False
        self.atacando = False
        self.tipo_ataque = 0
        self.cooldown_ataque = 0
        self.golpe = False
        self.vivo = True
        self.vida = 100
    
    def cargar_imagenes(self, hoja_sprites, pasos_animacion):
        lista_animacion = []
        for y, animacion in enumerate(pasos_animacion): 
            imagen_temp_lista = []
            for x in range(animacion):
                imagen_temp = hoja_sprites.subsurface(x * self.tamaño, y * self.tamaño, self.tamaño, self.tamaño)
                imagen_temp_lista.append(pygame.transform.scale(imagen_temp, (self.tamaño * self.escala_imagen,self.tamaño * self.escala_imagen)))
            lista_animacion.append(imagen_temp_lista)
        return lista_animacion
  
    #MOVIMIENTOS
    def mover(self, largo, alto, superficie, objetivo):
        velocidad = 10
        gravedad = 1
        dx = 0
        dy = 0
        self.corriendo = False
        self.tipo_ataque = 0

        key=pygame.key.get_pressed()

        #Solo moverse si no está atacando
        if self.atacando == False and self.vivo == True:
            #determinar los controles del jugador 1
            #JUGADOR 1
            if self.jugador == 1: 
                    
                #Movimiento
                if key[pygame.K_a]:
                    self.corriendo = True
                    dx=-velocidad
                if key[pygame.K_d]:
                    self.corriendo = True
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
            #JUGADOR 2
            if self.jugador == 2: 
                    
                #Movimiento
                if key[pygame.K_LEFT]:
                    self.corriendo = True
                    dx=-velocidad
                if key[pygame.K_RIGHT]:
                    self.corriendo = True
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
                    if key[pygame.K_o]:
                        self.tipo_ataque = 1
                    if key[pygame.K_p]:
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
        
        #Cooldown de ataque
        if self.cooldown_ataque > 0:
            self.cooldown_ataque -= 1

    #Actualizacion de animaciones
    def actualizar(self):
        #determinar que sprites necesita cada accion
        if self.vida <= 0: 
            self.vida = 0
            self.vivo = False 
            self.actualizar_accion(4) #Muerto

        elif self.golpe == True: 
            self.actualizar_accion(5) #Golpe o daño

        elif self.atacando == True:  
            if self.tipo_ataque == 1:
                self.actualizar_accion(1) #Ataque 1
            elif self.tipo_ataque == 2:
                self.actualizar_accion(1) #Ataque 2

        elif self.salto == True: 
            self.actualizar_accion(2) #Saltando

        elif self.corriendo == True:
            self.actualizar_accion(3) #Corriendo

        else: 
            self.actualizar_accion(0) #Idle

        animacion_cooldown = 20

        #actualiza la imagen
        self.imagen = self.lista_animacion[self.accion][self.frame_index] 

        #asegurar si paso tiempo suficiente desde la ultima actualización
        if pygame.time.get_ticks() - self.actualizacion > animacion_cooldown: 
            self.frame_index += 1
            self.actualizacion = pygame.time.get_ticks()

        #asegurar si la animación terminó
        if self.frame_index >=len(self.lista_animacion[self.accion]):
            self.frame_index = 0
           
            #asegurar si el ataque se realizó
            if self.accion == 1: 
                self.atacando = False
                self.cooldown_ataque = 30
            #asegurar si se tomó daño
            if self.accion == 5: 
                self.golpe = False
                self.atacando = False
                self.cooldown_ataque = 30

    def atacar(self, superficie, objetivo):
        if self.cooldown_ataque == 0:
            self.atacando = True
            atacante_rect = pygame.Rect(self.rect.centerx - (1 * self.rect.width * self.direccion) , self.rect.y, 1 * self.rect.width, self.rect.height)
            if atacante_rect.colliderect(objetivo.rect):
                objetivo.vida -=5
                objetivo.golpe = True
    
    #NUEVAS ACCIONES
    def actualizar_accion(self, nueva_accion):
        #determinar si la nueva accion es diferente a la anterior
        if nueva_accion != self.accion:
            self.accion = nueva_accion
            self.frame_index = 0
            self.actualizacion = pygame.time.get_ticks() 

    #DIBUJAR LOS PERSONAJES
    def dibujar(self,superficie):
        imagen = pygame.transform.flip(self.imagen, self.direccion, False)
        superficie.blit(imagen, (self.rect.x - (self.offset[0] * self.escala_imagen), self.rect.y - (self.offset[1] * self.escala_imagen)))
        

    