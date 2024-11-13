# Tipos de datos 
# Si queremos saber el tipo de dato ocupamos type()
# 1
palabra = "amigos"
tipo = type(palabra)
print(tipo)
# Salida = <class 'str'>

# 2
numero_int = 200
numero_int2 = 20_00_00_00
tipo2 = type(numero_int)
print(tipo2)
# Salida = <class 'int'>
print(numero_int2)
#Salida = 20000000

# 3 
numero_flot = 56.11
tipo3 = type(numero_flot)
print(tipo3)
# Salida = <class 'float'>

# 4
numero_grande = 999999999999
tipo4 = type(numero_grande)
print(tipo4)
#Salida = <class 'int'>

# Impresion de un entero
numerito = 200,99
tipoNum = type(numerito)
print(numerito)
print(tipoNum)
# Salida = (200, 99)
# Salida = <class 'tuple'>

# True and false (booleanos)
Registrado = True
tipo = type(Registrado)
print(tipo)
# Salida = <class 'bool'>
print(Registrado)
# Salida = True

# Casting tipo de datos
# Ejemplo 
automovil = "Lamborghini"
costo = "2_000_000_000"
puertas = 2
VelocidadMax = 300.50
Deportivo = True
Sedan = "False"

TipoDCosto = type(costo)
print(TipoDCosto)
# Salida = <class 'str'>

# Conversion de tipo de dato a entero
int_costo = int(costo)
print(int_costo)
# Salida = 2000000000
print(type(int_costo))
# Salida = <class 'int'>

# Conversion de tipo de dato a string
str_puertas = str(puertas)
print(str_puertas)
# Salida = 2
print(type(str_puertas))
# Salida = <class 'str'>

# Convertir bool a entero
depo = int(Deportivo)
print(depo)
# Salida = 1

# String a bool
sedanT = bool(Sedan)
print(sedanT)
# Salida = True
print(type(sedanT))
# Salida = <class 'bool'>