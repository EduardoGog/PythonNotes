# La entrada de un input() siempre pertenecera a la clase string
nombreUsuario = input("Cual es tu nombre de usuario?: ")
# Salida = Cual es tu nombre de usuario?: 
# Respuesta = Jose
print(nombreUsuario)
# Salida = Jose
print(type(nombreUsuario))
# Salida = <class 'str'>

edad = input("Que edad tienes?: ")
# Salida = Que edad tienes?:
print(edad)
# Salida = 15
print(type(edad))
# Salida = <class 'str'>

Bool = input("Verdadero o falso?: True o False \n")
# Salida = Verdadero o falso?: True o False
print(type(Bool))
# Salida = <class 'str'>

Cambio = bool(Bool)
print(type(Cambio))
# Salida = <class 'bool'>

int_edad = int(edad)
print(type(int_edad))