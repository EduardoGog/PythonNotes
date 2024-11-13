# Operadores lógicos
# and, or, not
# Ejemplo 
edad = int(input("Que edad tienes?: "))
genero = input("Hombre o mujer?: ")

# and
if edad >= 18 and genero == "hombre":
    print("Acceso garantizado a la zona de hombre")
elif edad >= 18 and genero == "mujer":
    print("Acceso garantizado a la zona de mujeres")

# or
elif edad < 18 or genero == "mujer":
    print("puedes acceder al baño publico de mujeres")
# elif edad < 18 or genero == "hombre":
#     print("puedes acceder al baño publico de hombres")
    
# not
print(not True)