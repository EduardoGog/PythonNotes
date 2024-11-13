# Los sets se usan para almacenar más de un item en una sola variable
# Los sets no pueden tener dos elementos 
# desordenadas, no se pueder cambiar, no tienen indices
# No se pueden cambiar pero sí eliminar y añadir nuevos items
# Ejemplo de un set
# set_ejemplo = {"abc", 34, True, 40, "male"}
deportes = set()
materias = {"matemáticas", "POO", "PIS", "Inglés"}
juegos = {"minecraft", "fortnite", "geometry dash", "clash royale"}
# print(deportes)

nuevo_set = {}
# print(type(nuevo_set))
# Salida = <class 'dict'>

# print(type(materias))
# Salida = <class 'set'>

# print(materias)
# Salida = {'PIS', 'POO', 'Inglés', 'matemáticas'}

metodos_set = dir(deportes)
# print(metodos_set)

# 'add', 'clear', 'copy', 'difference', 'discard', 'intersection', 'pop', 'remove','union', 'update'

# Metodo add
materias.add("Alemán")
print(materias)
# Salida = {'PIS', 'matemáticas', 'Alemán', 'POO', 'Inglés'}

# Método clear
materias.clear()
print(materias)
# Salida = set()

# Método copy
copia = juegos.copy()
print(copia)
# Salida = {'fortnite', 'geometry dash', 'clash royale', 'minecraft'}

# Método difference
diferencia = materias.difference(juegos)
print(diferencia)
# Salida = {'Inglés', 'PIS', 'POO', 'matemáticas'}

# Método discard
juegos.discard("clash royale")
print(juegos)
# Salida = {'minecraft', 'fortnite', 'geometry dash'}

# Método intersección
letras = {"a", "b", "c", "d", "e"}
vocales = {"a", "e", "i", "o" "u"}
interseccion = letras.intersection(vocales)
print(interseccion)
# Salida = {'a', 'e'}

# Método pop
juegos.pop()
print(juegos)
# {'geometry dash', 'fortnite'}
# Elimina un objeto random

# Método remove
marcas = {"nike", "adidas", "north face"}
marcas.remove("nike")
print(marcas)
# Salida = {'adidas', 'north face'}

# Método union
colores = {"azul", "blanco", "rojo"}
colores2 = {"dorado", "plateado"}
union = colores.union(colores2)
print(union)
# Salida = {'rojo', 'dorado', 'azul', 'plateado', 'blanco'}

# Método update
notas = {10, 11, 45, 100}
notas2 = {9, 8, 6, 6}

notas.update(notas2)
print(notas)
# Salida = {100, 6, 8, 9, 10, 11, 45} 


