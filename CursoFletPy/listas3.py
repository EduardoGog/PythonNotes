# Listas anidadas

secuencia = [True, "John", [56, 78], "chris", [True, ["Carlos", "John", 78], 90.66]]
ultimo_elemento = secuencia[-1]
print(ultimo_elemento)
# Salida = [True, ['Carlos', 'John', 78], 90.66]

# Obtener elemento de una lista anidada
elemento_anidado = ultimo_elemento[1]
print(elemento_anidado)
# Salida = ['Carlos', 'John', 78]

ultimo_anidado = elemento_anidado[-1]
print(ultimo_anidado)
# Salida = 78

# Otra manera de hacerlo 
print(secuencia[-1][1][-1])
# Salida = 78

