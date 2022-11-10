import pygame
from funcionesVACIAS import *
from pygame.locals import *
from configuracion import *


def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    #elif key == K_MINUS:
        #return("-")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")

def seleccionDeDificultad(screen):
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)

    screen.blit(defaultFont.render("Selección de dificultad", 1, COLOR_TEXTO), (15, 15))
    screen.blit(defaultFont.render("[1]. Fácil", 1, (0, 200, 0)), (15, 50))
    screen.blit(defaultFont.render("[2]. Intermedio - Palabras de longitud intermedia o largas", 1, (170, 200, 0)), (15, 80))
    screen.blit(defaultFont.render("[3]. Difícil - Palabras largas, mayor penalización por errores", 1, (200, 0, 0)), (15, 110))
    screen.blit(defaultFont.render("Seleccioná un número con el teclado", 1, COLOR_TEXTO), (15, 400))

def dibujar(screen, palabraUsuario, palabraActual, puntos, segundos):

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    #Linea Horizontal
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    #muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_TEXTO), (190, 570))
    #muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO), (680, 10))
    #muestra los segundos y puede cambiar de color con el tiempo
    if(segundos<15):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (10, 10))

    #muestra la palabra
    screen.blit(defaultFontGrande.render(palabraActual, 1, COLOR_LETRAS), (ANCHO//2-len(palabraActual)*TAMANNO_LETRA_GRANDE//4,ALTO-400))






