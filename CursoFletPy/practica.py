# Programa de practica, sorte de servicio militar
# Generar matriculas aleatorias
# Escoger matriculas aleatorias
# Buscar matriculas para verificar la bola correspondiente
# Imprimir mensaje correspondiente
import random
lista_sorteo = []
print("Bienvenido al sistema de servicio militar...")
encuadre = input("Dame las matriculas a sortear, separadas por coma y espacio (0 - 15): ")
lista_encuadrados = encuadre.split(",")
sorteo = random.choice(lista_encuadrados)
print("Veamos qué bola te ha tocado...")
busqueda = input("Dame tu matricula (0 - 15): ")
if(sorteo == busqueda):
    print("Te ha tocado marchar...")
elif(sorteo != busqueda):
    print("Te salvaste, te tocó bola negra...")
elif busqueda not in lista_encuadrados:
    print("Digita una matricula en el rango (0 - 15)")




