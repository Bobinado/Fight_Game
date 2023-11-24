import pygame
#Cuenta regresiva (3, 2, 1)
def cuenta_regresiva(screen, intro, font, color, largo, alto):
    #Renderizar el texto
    text_render = font.render(f"{intro}", True, color)
    go = font.render("FIGHT!", True, color)
    #Posición del texto en la ventana
    text_rect = text_render.get_rect()
    text_rect.center = (largo // 2, alto // 2)

    #Solo mostrar el texto hasta que llegue a 0
    if intro > 0:
        #Dibujar el texto en la pantalla
        screen.blit(text_render, text_rect) 