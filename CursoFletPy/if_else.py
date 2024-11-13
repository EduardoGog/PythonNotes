# Operadores
# ==, <, >, !=, <=, >=
# Ejemplo
precio = 50_000
saldo = 30_000

# <, >
if saldo < precio:
    print("No tienes suficiente saldo")
else:
    print("Puedes comprar tu producto")

# Con un saldo de 30_000
    # Salida = No tienes suficiente saldo
# Con un saldo de 70_000
    # Salida = Puedes comprar tu producto

# ==, !=
cuenta = 125_000
costo = 126_000

if cuenta == costo:
    print("Puedes adquirir el producto")
else:
    print("No tienes suficientes fondos")

# Con un saldo de 125_000 en la cuenta
    # Salida = No tienes suficientes fondos
# Con un saldo de 126_000 en la cuenta
    # Salida = puedes adquirir el producto

respuesta = input("Quieres iniciar sesion?: ")
if respuesta != "si":
    print("Puedes registrarte")
else:
    print("Bienvenido a la pagina")

# En caso de responder "si"
    # Salida = "Bienvenido a la pagina"
# En caso de responder "no"
    # Salida = "Puedes registrarte"

# <=, >=
calificacion = input("Dame la calificacion que obtuviste: ")
convert = int(calificacion)
if convert <= 5:
    print("Has reprobado el curso :(")
else:
    print("Aun tienes oportunidad de pasar :)")

# Si tu respuesta es 5
    # Salida = "Has reprobado el curso :("
# En caso de que hayas puesto 6
    # Salida "Aun tienes oportunidad de pasar :)"


