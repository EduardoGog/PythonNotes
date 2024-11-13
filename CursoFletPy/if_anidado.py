# Identacion en python
# En una condicional if la identacion es importante
# Para evitar errores de sintaxis
# Ejemplo 
#   if 5 > 4:
#   print("True") -> incorrecto
#   if 5 > 4:
#       print("True") - > correcto

# if, else, if elif else
capacidad = 5_000
if capacidad >= 20_000:
    print("Tienes un lugar")
elif capacidad >= 5000:
    print("Espacio limitado")
elif capacidad == 3000:
    print("Apenitas")
else:
    print("No puedes pasar")

# Si tenemos una capacidad de 30_000
    # Salida = "Tienes un lugar"
# capacidad = 6000
    # Salida = "Espacio limitado"
# Capacidad = 4500
    # Salida = "No puedes pasar"
# Capacidad = 3000
    # Salida = "Apenitas"

# Otro ejemplo
fruta = input("Nombre de fruta: ")
if fruta == "manzana":
    print("precio: $35 kg")
elif fruta == "mango":
    print("precio: $40 kg")
elif fruta == "platano":
    print("precio: $25 kg")
else:
    print("No tenemos la fruta solicitada")


