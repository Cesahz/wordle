#-----1-Variables globales
#Crear una lista de palabras posibles para el juego
lista_palabras = [
    "altura", "blanco", "camino", "dormir", "espejo",
    "fuerza", "gritar", "hierro", "jardin", "lluvia",
    "mañana", "noches", "origen", "puerta", "quesos",
    "ratonz", "suerte", "tierra", "unidos", "viento"
]
numero_elegido = int(input('Ingresa un numero del 1 al 20 para elegir una palabra: '))

palabra_elegida = lista_palabras[numero_elegido - 1]

limite_letra = 6

intentos = 6

jugando = True