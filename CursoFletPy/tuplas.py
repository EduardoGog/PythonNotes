# Tuplas en python
# Usadas para guardar multiples items en una sola variable
# Uno de los 4 tipos de datos que almacenan informacion
# Otros: listas, set, diccionarios
# Las tuplas van encerradas por ()
# Ordenadas y nunca cambian
# ejemplo de tupla
frutas = ("platano", "mango", "fresas", "coco")
e_commerce = ("shopify", "amazon", "mercado libre", "ebay")
e_commerce_type = type(e_commerce)
print(e_commerce_type)
# Salida = <class 'tuple'>
print(dir(e_commerce))

# Accedemos a los indices como en las listas mediante []
shopify = e_commerce[0]
print(shopify)
# Salida = shopify

# funciones_tupla = dir(e_commerce)
# print(funciones_tupla)

# Count function
item_count = e_commerce.count("shopify")
print(item_count)
# Salida = 1

# Index function
item_index = e_commerce.index("ebay")
print(item_index)
# Salida = 3

# Para desempacar un elemento dentro de una tupla
# Se asignan variables.
primera, segunda, tercera, cuarta = frutas
print(primera)
# Salida = platano

# Para desempacar mas de un elemento
comercio1, comercio2, *demas = e_commerce
print(demas)
# Salida con * = mercado libre ebay
# Salida sin * = ['mercado libre', 'ebay']
print(type(demas))
# Saldia = <class 'list'>
