# Actualización de un elemento en una lista

# lenguajes_progra = ["Java", "C++", "C", "Python", "Javascript", "C#"]
# C_sharp = lenguajes_progra[-1]
# print(C_sharp)

# lenguajes_progra[-1] = "Rubi"
# print(lenguajes_progra)
# Salida = ['Java', 'C++', 'C', 'Python', 'Javascript', 'Rubi']

# Lista anidada
secuencia = [True, "John", [56, 78], "chris", [True, ["Carlos", "John", 78], 90.66]]
carrito = ["Macbook","Airpods", "Papel de baño", "Queso amarillo"]

# lista_de_operaciones = dir(carrito)
# print(lista_de_operaciones)

# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# append
# carrito.append("Cuaderno")
# print(carrito)
# Salida = ['Macbook', 'Airpods', 'Papel de baño', 'Queso amarillo', 'Cuaderno']

# clear
# carrito.clear()
# print(carrito)
# Salida = []

# copy
# copia = carrito.copy()
# print(copia)

#count
# carrito.append("Papel de baño")
# total_elementos = len(carrito)
elemento_especifico = carrito.count("Papel de baño")
# print(total_elementos)
# # salida = 6
print(elemento_especifico)
# Salida = 1

# extend
mini_carrito = ["monitor", "teclado"]
# carrito.append(mini_carrito)
# print(carrito)
# Salida = ['Macbook', 'Airpods', 'Papel de baño', 'Queso amarillo', ['monitor', 'teclado']]
carrito.extend(mini_carrito)
print(carrito)
# Salida = ['Macbook', 'Airpods', 'Papel de baño', 'Queso amarillo', 'monitor', 'teclado']

# index
index = carrito.index("Queso amarillo")
print(index)
# Salida = 3
print(carrito[3])

# insert
carrito.insert(0, "Mouse")
print(carrito)
# Salida = ['Mouse', 'Macbook', 'Airpods', 'Papel de baño', 'Queso amarillo', 'monitor', 'teclado']

# pop
carrito.pop()
print(carrito)
# Salida = ['Mouse', 'Macbook', 'Airpods', 'Papel de baño', 'Queso amarillo', 'monitor'] # Elimina el ultimo elemento en el utlimo inidice
carrito.pop(0)
print(carrito)
# Salida = ['Macbook', 'Airpods', 'Papel de baño', 'Queso amarillo', 'monitor'] # Podemos especificar un indice en especifico

# Remove
carrito.remove("Queso amarillo")
print(carrito)
# Salida = ['Macbook', 'Airpods', 'Papel de baño', 'monitor']

# Reverse
carrito.reverse()
print(carrito)
# Salida = ['monitor', 'Papel de baño', 'Airpods', 'Macbook']

# sort
numeros = [4, 5, 1, 8]
numeros.sort()
print(numeros)
# Salida = [1, 4, 5, 8]

carrito.sort()
print(carrito)
# Salida = ['Airpods', 'Macbook', 'Papel de baño', 'monitor'] # Ordenado alfabeticamente
