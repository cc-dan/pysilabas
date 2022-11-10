#! /usr/bin/env python
# coding=utf-8

import os, random, sys, math

import pygame
from pygame.locals import *
from configuracion import *
from extras import *
from funcionesSeparador import *

from funcionesVACIAS import *

#Funcion principal
def main():
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        pygame.mixer.init()

        # -- Sonidos
        sonidoExito = pygame.mixer.Sound('sonidos/success.wav')
        sonidoError = pygame.mixer.Sound('sonidos/fail.mp3')

        #Preparar la ventana
        pygame.display.set_caption("El juego del Mago Goma...")
        screen = pygame.display.set_mode((ANCHO, ALTO))

        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial

        puntos = 0
        palabra = ""
        listaPalabrasDiccionario=[]
        ultimaLetra = ""
        letra = ""
        cantidadDeTeclasApretadas = 0
        tiempoComienzoRespuesta = 0
        tiempoEnResponder = 0
        longitudMinimaDePalabras = 4
        tiempoComienzo = 0
        dificultad = DIFICULTAD_INICIAL

        archivo= open("lemario.txt","r")

        #lectura del diccionario
        lectura(archivo, listaPalabrasDiccionario) # guardamos las palabras del lemario en listaPalabrasDiccionario
        valorLongitudMaximo = palabraMasLarga(listaPalabrasDiccionario) # usamos listaPalabrasDiccionario para saber cuál es la palabra más larga
##
        seleccionDeDificultad(screen) # -- Dibujamos el menu de selección de dificultad

        while segundos > fps/1000:
            # 1 frame cada 1/fps segundos
            gameClock.tick(fps)

            # Empezamos a contar 
            totaltime += gameClock.get_time()

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():
                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    # --- Punto de entrada. Se selecciona la dificultad
                    if dificultad == -1:
                        if e.key == K_1:
                            dificultad = 1
                        if e.key == K_2:
                            dificultad = 2
                        if e.key == K_3:
                            dificultad = 3

                        # -- Configuramos la longitud de las palabras y generamos la primera palabra
                        longitudMinimaDePalabras *= dificultad
                        palabraEnPantalla=nuevaPalabra(listaPalabrasDiccionario, longitudMinimaDePalabras, valorLongitudMaximo)

                        # -- Anotamos el tiempo en el que empezó el juego
                        tiempoComienzo = totaltime / 1000

                    if dificultad != -1:
                        # -- Queremos contar cuántas teclas usó el jugador para su respuesta, sin contar la tecla enter
                        if not e.key == K_RETURN: 
                            cantidadDeTeclasApretadas += 1
                        
                        ultimaLetra = letra # -- Anotamos la letra para luego chequear que si es un espacio, no se repita
                        letra = dameLetraApretada(e.key)

                        if not(letra==" " and letra==ultimaLetra): # -- CONDICIÓN para evitar que las silabas se separen con más de un espacio (mantiene el formato)
                            #Si la última letra fue un espacio, no permitir agregar otro espacio. 
                            palabra += letra #es la palabra que escribe el usuario

                        if e.key == K_BACKSPACE:
                            palabra = palabra[0:len(palabra)-1]
                        if e.key == K_RETURN:
                            #pasa la palabra a silabas
                            palabraEnPantallaEnSilabas=palabraTOsilaba(palabraEnPantalla)

                            # -- Anotamos el tiempo que le tomó responder
                            tiempoEnResponder = (totaltime - tiempoComienzoRespuesta) / 1000

                            # -- Aplicamos la puntuación adecuada en base a la palabra, el tiempo en responder, si acertó o no, y la cantidad de teclas apretadas
                            puntos += calcularPuntaje(palabraEnPantalla, tiempoEnResponder, esCorrecta(palabraEnPantallaEnSilabas, palabra), cantidadDeTeclasApretadas, dificultad)
                            
                            # -- Reproducimos los sonidos
                            if esCorrecta(palabraEnPantallaEnSilabas, palabra):
                                pygame.mixer.Sound.play(sonidoExito)
                            else:
                                pygame.mixer.Sound.play(sonidoError)

                            # Reiniciamos el contador de tiempo de respuesta
                            tiempoComienzoRespuesta = totaltime

                            # Se elige una nueva palabra
                            palabraEnPantalla=nuevaPalabra(listaPalabrasDiccionario, longitudMinimaDePalabras, valorLongitudMaximo * dificultad)

                            # Se limpia el input del jugador
                            palabra = ""
                            cantidadDeTeclasApretadas = 0
                        
            if dificultad != -1: 
                segundos = (tiempoComienzo + TIEMPO_MAX) - pygame.time.get_ticks()/1000

            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)

            #Dibujar de nuevo todo
            if dificultad != -1:
                dibujar(screen, palabra, palabraEnPantalla, puntos,segundos)
            else:
                seleccionDeDificultad(screen)

            pygame.display.flip()

        pygame.mixer.quit()

        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return

        archivo.close()
#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()
