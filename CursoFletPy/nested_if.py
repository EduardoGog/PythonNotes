# Progranma de if anidado
# Primer ejemplo

# numero = int(input("Digita un numero: "))
# if numero < 0:
#     print("El numero es negativo")
# else:
#     if numero == 0:
#         print("El numero es cero")
#     else:
#         print("El numero es positivo")

# Segundo ejemplo
respuesta = input("¿Tienes hmabre?: ")
if respuesta == "si":
    print("Ve a la tienda.")
    costo = int(input("¿Cuanto cuesta este chocolate?: "))
    if costo <= 1:
        print("Comprare 3")
    else:
        print("Comprare 1")
elif respuesta == "no":
    print("Quedate en casa")
    hobbie = input("¿Quieres jugar fortnite?: ")
    if hobbie == "si":
        print("Nos vemos la siguiente semana")
    else:
        print("Ve a estudiar")
        materia = input("¿Cual es tu materia favorita?: ")
        if materia == "Computacion":
            print("Tambien es mi materia favorita")
        else:
            print("No tenemos nada en comun")
else:
    print("Respuesta invalida")
