# Importacion de nuestro mudulo contenedor de funciones
# import banco

# Otra forma de importación de "todo"
# from banco import *

# Total de usuarios
# Llamado al método de total_usuarios
# Cuando usamos import banco
# print(banco.total_usuarios())

# Cuando usamos from banco import *
# print(total_usuarios())

# Importar una función específica

# from banco import usuarios, total_usuarios, borrrar_usuario
# print(total_usuarios())
# print(usuarios)

# Uso de la palabra "as"

# from banco import usuarios as us
# # as se puede usar como un alias o un renombramiento
# print(us)

# nuevos_usuarios = ["Manuel", "Carlos", "Michelle"]
# print(nuevos_usuarios)

# Modulo random
import random
import banco
# from bank import usuarios

# Metodo dir
# abreviacion de directory
# Muestra las funciones disponibles
todas_las_funciones = dir(random)
print(todas_las_funciones)





