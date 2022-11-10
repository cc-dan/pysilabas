from principal import *
from configuracion import *
import random
from funcionesSeparador import separador

def lectura(archivo, salida):
    for linea in archivo.readlines(): # iteramos sobre la lista de renglones que nos devuelve la función readlines()
        salida.append(linea[:-1]) # añadimos cada linea a la lista 'salida', pero recortados su último caracter (\n). Esto se hace seleccionando de la cadena 'linea' sus caracteres desde la posición 0 a la -1

def palabraMasLarga(lista):
    # función para encontrar la palabra más larga del lemario, con el fin de poner limites al exigir una longitud mínima de palabras
    masLargo = 0

    for palabra in lista:
        if len(palabra) > masLargo: 
            masLargo = len(palabra)

    return masLargo

def nuevaPalabra(lista, longitudMinimaDePalabras, valorLongitudMaximo): # incorporamos la funcionalidad de longitud minima de palabras
    if longitudMinimaDePalabras > valorLongitudMaximo: # para asegurarnos que no se puedan pedir palabras más largas de las que hay en el lemario
        longitudMinimaDePalabras = valorLongitudMaximo

    indexListaPalabras = random.randint(0, len(lista)-1) # generamos un número al azar dentro de los límites de la lista

    while len(lista[indexListaPalabras]) < longitudMinimaDePalabras: # chequeamos si en ese index random la palabra cumple la longitud minima
        indexListaPalabras = random.randint(0, len(lista)-1) # si no lo cumple, seguimos generando numeros
    
    return lista[indexListaPalabras]

def silabasTOpalabra(palabraEnSilabas):
    # recibe una palabra separada en silabas y devuelve la palabra sin espacios

    palabra = "" # declaramos la variable que vamos a retornar, vacia porque va a ir tomando los caracteres de palabraEnSilabas

    for char in palabraEnSilabas: # iteramos sobre los caracteres de la cadena palabraEnSilabas
        if not (char == " "): # no tenemos en cuenta a los espacios
            palabra += char # vamos transcribiendo palabraEnSilabas a la variable palabra

    return palabra

def palabraTOsilaba(palabra):
    return separador(palabra) # retornamos la cadena que nos devuelve la funcion separador(), que cumple la función de separar una palabra en sílabas

def esCorrecta(palabraEnSilabasEnPantalla, palabra):
    return palabra == palabraEnSilabasEnPantalla

    """
    Una solución alternativa que pensé fue programar la función estandarizarPalabraEnSilabas() para
    pasar el input del usuario al formato de la función separador() (separada con guiones) pero me 
    pareció más prolijo setear reglas para limitar el input del usuario. Estas son:
        - Evitar que se utilize más de un espacio para separar las silabas (en principal.py)
        - Eliminar la opción de utilizar un guion (KP_MINUS) en extras.py
    En el otro caso, se usaría 'return estandarizarPalabraEnSilabas(palabra) == palabraEnSilabasEnPantalla'
    La función está comentada más abajo.
    """

def calcularPuntaje(palabra, tiempoEnResponder, palabraAcertada, cantidadDeTeclasApretadas, dificultad):
    if not palabraAcertada: return -5 * dificultad # devolvemos un valor fijo en caso de cualquier equivocación

    # a partir de tiempoMaximoRespuestaRapida (segundos) no hay bonificacion por tiempo. Se consideran 400 milisegundos por letra, más un márgen de 500 milisegundos extra
    tiempoMaximoRespuestaRapida = len(palabra) * TIEMPO_POR_LETRA_EXIGIDO + 0.5

    # consideramos el numero maximo entre 0 y la diferencia entre el tiempo maximo y el tiempo de respuesta. Si se supera el tiempo maximo, la resta será negativa y el número máximo será 0, que al multiplicar por los puntos los anula. 
    bonificacionRespuestaRapida = int((max(0, tiempoMaximoRespuestaRapida - tiempoEnResponder) ** PUNTOS_POR_SEGUNDO))
    # Se suman además puntos por la longitud de la palabra. Este es aplicable aunque se supere el tiempo máximo de la bonificación por tiempo
    puntosPorTiempoRespuesta = (len(palabra)//2)//tiempoEnResponder
    # Puntaje por no hacer correciones. Convirtiendo al booleano en un entero, el valor 0 se corresponde a falso. Entonces, los puntos se anulan cuando la cantidad de teclas apretadas no coincide con la palabra a escribir
    puntosPorPerfeccion = cantidadDeTeclasApretadas//3 * int(cantidadDeTeclasApretadas == len(palabraTOsilaba(palabra)))

    # Sumamos todas las bonificaciones en un entero
    puntajeBonus = int(bonificacionRespuestaRapida + puntosPorTiempoRespuesta + puntosPorPerfeccion) // dificultad
    
    print("Respuesta en", tiempoEnResponder, "segundos")
    print("BONIFICACIÓN DE TIEMPO:", bonificacionRespuestaRapida)
    print("PUNTOS POR LONGITUD:", puntosPorTiempoRespuesta)
    print("PUNTOS POR PERFECCIÓN: ", puntosPorPerfeccion)
    print("TOTAL:", 1 + puntajeBonus)
    
    return 1 + puntajeBonus # el puntaje base es 1. Si no se cumple con ningún extra, ese será el valor de la respuesta correcta.

def estandarizarPalabraEnSilabas(palabraEnSilabas):
    # NO UTILIZADA, conservada a modo de ejemplo
    # su propósito es transformar el input del usuario al formato que maneja la función separar()

    char = 0
    palabra = ""

    while char < len(palabraEnSilabas): # iteramos sobre la palabra
        if palabraEnSilabas[char] == ' ' or palabraEnSilabas[char] == "-": # si nos encontramos con un espacio
            palabra += '-' # reemplazamos ese espacio por un guion
            char += 1 # avanzamos al proximo caracter

            while (palabraEnSilabas[char] == " " or palabraEnSilabas[char] == "-"): # si este nuevo caracter es también un espacio
                char +=1 # avanzamos sin agregarlo a la nueva cadena
        else: 
            palabra += palabraEnSilabas[char] # si no es un espacio, agregamos el caracter como está
            char +=1

    return palabra