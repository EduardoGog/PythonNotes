# Modulo random
import random
import banco
# from bank import usuarios

nombres = ["John", "Elias", "Pancho"]
calificaciones = [10, 5, 8, 6, 9, 7, 10]

# Metodo dir
# abreviacion de directory
# Muestra las funciones disponibles
# todas_las_funciones = dir(random)
# print(todas_las_funciones)

# CHOICE

# choice, random, randint, shuffle, randbytes y seed
# Choice -> funcion dentro de random
# Itera en una lista de objetos y selecciona uno aleatoriamente
# nombre_aleatorio = random.choice(nombres)
# calificacion_aleatoria = random.choice(calificaciones)
# print(nombre_aleatorio)
# print(calificacion_aleatoria)

# RANDOM

# Es usado cuando queremos un numero aleatorio con punto flotante
# random no toma ningun parametro

# flotante_aleatorio = random.random()
# print(flotante_aleatorio)
# Salida = 0.3518196166015325

# RANDINT

# entero_aleatorio = random.randint(0, 10)
# print(entero_aleatorio)
# Salida 4

# SHUFFLE
# Intercambia posiciones en estructuras iterables

random.shuffle(nombres)
print(nombres)
# Salida = ['John', 'Pancho', 'Elias']
# Salida = ['Pancho', 'Elias', 'John']

random.shuffle(calificaciones)
print(calificaciones)


# SEED 
# Guarda el estado de un número aleatorio
# Ejemplo 1
random.seed(1)
votos_random = random.randint(50, 100)
print(votos_random)
# Salida con seed descomentado = 74
# Salida con seed comentado = 68, 75    

# Ejemplo 2
# random.seed(0)
# ganador = random.choice(nombres)
# print(ganador)

# Salida = Elias