# Operador ternario evalua algo basado en una condicion
# Siendo verdadero o falso
# Remplazando if - else para hacer más compacto el código

# Ejemplo
# a = 10
# b = 20

# min = a if a < b else b
# print(min)
# Salida 10

# lenguaje = input("¿Cual es tu lenguaje de programacion favorito?: ")
# if lenguaje == "python" : print("Buena opcion") 

# Ejemplo 2
piel = input("¿Que color de piel tienes?: ")
color = "blanca" if piel == "blanca" else "negra"
print(color)
# Salida si respuesta es "blanca"
# blanca
# Salida si respuesta es "negra"
# negra

# Ejemplo 3
gusto = input("¿Te gusta programar?: ")
si = "Hay que seguir practicando mas"
no = "Tienes que estudiar y practicar mas"
respuesta = si if gusto == "si" else no
print(respuesta)
# Salida si respuesta es si
# Hay que seguir practicando mas
# Salida si respuesta es no
# Tienes que estudiar y practicar mas