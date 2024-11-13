# Introducir una lista de autos separados por comas y espacios
import random
# Mi solución
# print("Bienvenido de nuevo al programa que escoje carros")
# valores = input("Ingresa nombres de carros separados por comas: ")
# valores_lista = valores.split(",")
# # print(valores_lista)
# aleatorio = random.choice(valores_lista)
# frase = f"Deberias comprar un {aleatorio}"
# print(frase)

# Solucion Philip
print("Bienvenido al programa escogedor de autos!")
# 1 obtener el string de carros
carros = input("Digita nombres de autos separados por comas y espacios: ")
# 2 hacer split al string
lista_carros = carros.split(", ")
# print(lista_carros)
# 3 escojer un coche random de la lista
random_car = random.choice(lista_carros)
# 4 imprime el auto random
print(f"Deberias obtener un {random_car}")