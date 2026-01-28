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

#------2-Definir funciones para el juego

#Pedimos la palabra y verificamos que solo tenga 6 letras, tambien restamos un intento por cada palabra ingresada
def Solicitar_palabra():
    ingresar_palabra = input('Escribe una palabra: ')
    while len(ingresar_palabra) != len(palabra_elegida):
        print('La palabra tiene que tener 6 letras, vuelve a escribir otra palabra: ')
        ingresar_palabra = input('Escribe otra palabra que tenga 6 letras: ')
    return ingresar_palabra

#Resaltar las letras que coinciden
def Resaltar_letra(palabra_puesta,palabra_clave):
    letras = []
    for i in range(limite_letra):
        letra_p = palabra_puesta[i]
        letra_c = palabra_clave[i]
        if letra_p == letra_c:
            letras.append(f'[{letra_p}]')
        elif letra_p in palabra_clave:
            letras.append(f'({letra_p})')
        else:
            letras.append(f'{letra_p}')
    return letras

#Creo una funcion para controlar los intentos
def Controlar_intentos(intento_actual):
    if intento_actual < 1:
        sigo_jugando = False
        return sigo_jugando
    else:
        sigo_jugando = True
        return sigo_jugando

#Avisar si ganamos o perdimos
def Resultado_juego():
    if not jugando:
        print('Perdiste el juego. \n ')
    elif palabra_elegida == palabra_ingresada:
        print(f'Ganaste el juego, te tomo solo {6 - intentos} intentos \n')
        sigo_jugando = False
        return sigo_jugando
    else:
        sigo_jugando = True
        return sigo_jugando

#-----Iniciamos el juegoo
while jugando:
    palabra_ingresada = Solicitar_palabra()
    letras_verificadas = Resaltar_letra(palabra_ingresada,palabra_elegida)
    print(f'{letras_verificadas}')
    intentos -= 1
    jugando = Controlar_intentos(intentos)
    if jugando:
        print(f'Tienes {intentos} intentos.')
        jugando = Resultado_juego()
    else:
        jugando = Resultado_juego()