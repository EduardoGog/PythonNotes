# Ejercicio 1
# Pide al usuario que ingrese dos números
# Suma los números e imprime el resultado

# numero_uno = int(input("Dame un numero: "))
# numero_dos = int(input("Dame otro numero: "))
# suma = numero_uno + numero_dos
# print(f"La suma de {numero_uno} + {numero_dos} es: {suma}")

# Ejercicio 2
# Pide al usuario que ingrese un número
# Verifica si el número es par o impar e imprime el resultado

# num = int(input("Dame un numero para verificar si es par: "))
# if num % 2 == 0:
#     print("El numero es par")
# else:
#     print("El numero es impar")

# Ejercicio 3
# Pide al usuario que ingrese una palabra
# Cuenta el número de letras en la palabra e imprime el resultado

# palabra = input("Dame una palabra: ")
# print(len(palabra))

# Ejercicio 4
# Pide al usuario que ingrese una cadena
# Invierte la cadena e imprime el resultado

# Pide al usuario que ingrese una cadena
# cadena = input("Dame una cadena: ")

# # Invierte la cadena usando rebanado
# cadena_invertida = cadena[::-1]

# # Imprime el resultado
# print(f"La cadena invertida es: {cadena_invertida}")

# Otra manera:
# Pide al usuario que ingrese una cadena
cadena = input("Dame una cadena: ")

# Inicializa una cadena vacía para la cadena invertida
cadena_invertida = ""

# Itera sobre cada carácter en la cadena original
for caracter in cadena:
    # Agrega cada carácter al principio de la cadena invertida
    cadena_invertida = caracter + cadena_invertida
    # Debug: Muestra cómo se construye la cadena invertida paso a paso
    print(f"Caracter: {caracter}, Cadena invertida actual: {cadena_invertida}")

# Imprime el resultado final
print(f"La cadena invertida es: {cadena_invertida}")




# Ejercicio 5
# Pide al usuario que ingrese tres números
# Encuentra el mayor de los tres números e imprime el resultado

# primero = int(input("Dame el numero 1: "))
# segundo = int(input("Dame el numero 2: "))
# tercero = int(input("Dame el numero 3: "))
# if primero > segundo & primero > tercero:
#     print(f"El numero mas grande es {primero}")
# elif segundo > primero & segundo > tercero:
#     print(f"El numero mas grande es {segundo}")
# elif tercero > primero & tercero > segundo:
#     print(f"El numero mas grande es {tercero}")



