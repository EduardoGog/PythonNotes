# El bucle for
# Utilizado para iterar sobre una secuencia
# Pero... ¿Qué es una secuencia?
# En python es un tipo de dato que contiene una colección de elementos
# e.j enteros, floats, strings, listas y más
# Ejemplo, suponiendo que tenemos la siguiente lista 
frutas = ["peras", "platanos", "mangos", "fresas"]
# Sintáxis básica 
# for x in frutas:
#     print(x)

divisas = ["Euro", "MXN", "Dolar", "Rupia"]
paises = ("Mexico", "España", "China", "Alemania")
lenguajesP = {"python", "C", "C++", "java"}
email = "eduardo.glez7828@gmail.com"

# for div in divisas:
#     print(div)
# # Salida =  # Euro
#             # MXN
#             # Dolar
#             # Rupia

for pais in paises:
    print(pais.upper())
# # Salida =  MEXICO
#             ESPAÑA
#             CHINA
#             ALEMANIA

for lenguaje in lenguajesP:
    # print(lenguaje)
# Salida  = 
# C
# python
# java
# C++

    logitud_nombre = len(lenguaje)
    print(f"{lenguaje} tiene una longitud de caracteres de {logitud_nombre}")
# Salida
# C++ tiene una longitud de caracteres de 3
# C tiene una longitud de caracteres de 1
# java tiene una longitud de caracteres de 4
# python tiene una longitud de caracteres de 6

#Poner en mayuscula primera letra de cada elemento de una lista
# for i in frutas:
#     # print(i.capitalize())
#     mayus = i.upper()
#     lista = list(i)
#     lista[0] = lista[0].upper()
#     print("".join(lista))
    
# for char in email:
#     print(char)

    

