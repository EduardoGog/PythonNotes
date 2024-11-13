# Funciones de Strings como listas
profesiones = ["Programador de backend", "Programador de frontend"]
nombre = "Eduardo"
saludo = "buenos dias a todos :)"
despedida = "ADIOS AMIGOS, QUE LES VAYA BIEN :)"
calificaciones = "10,9,8,5,6,7,10,9"

# funciones_lista = dir(profesiones)
# print(funciones_lista)

# funciones_string = dir(nombre)
# print(funciones_string)

# Funciones: capitalize, count, endswith, index, replace, title, upper, split, lower, islower, isupper

# capitalize -> Mayuscula en el primer caracter
capitalized_nombre = nombre.capitalize()
print(capitalized_nombre)
# Salida = Eduardo

# count -> cuenta letras en especifico
conteo_caracter = nombre.count("d")
print(conteo_caracter)
# Salida = 2

# endswith
if nombre.endswith("o"):
    print("Nombre termina con caracter o")
else:
    print("El nombre no termina con caracter o")

# Salida = Nombre termina con caracter o

# startswith
if nombre.startswith("e"):
    print("Mi nombre empieza con e")
else:
    print("Mi nombre no empieza con e, empieza con E")

# Salida = Mi nombre no empieza con e, empieza con E

# index
print(nombre.index("o"))

# Salida = 6

# Replace
nombre_modificado = nombre.replace("E","e")
print(nombre_modificado)
# Salida = eduardo

print("Capitalize")
# tittle -> similar a capitalize
tittle_nombre = nombre.title()
print(tittle_nombre)
# Salida = Eduardo

# upper
upper_frase = saludo.upper()
print(upper_frase)
# Salida = BUENOS DIAS A TODOS :)

# lower
lower_frase = despedida.lower()
print(lower_frase)
# Salida = adios amigos, que les vaya bien :)

# split
separar_calificaciones = calificaciones.split(",")
print(separar_calificaciones)
# Salida = ['10', '9', '8', '5', '6', '7', '10', '9']

# islower
es_minuscula = nombre.islower()
print(es_minuscula)
# Salida = False

# isupper
es_mayuscula = despedida.isupper()
print(es_mayuscula)
# Salida = True
