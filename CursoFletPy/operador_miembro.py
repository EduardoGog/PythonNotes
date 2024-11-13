# Verificar si un elemento pertenece a un grupo en específico
# not in, in
paises_europeos = ['Alemania', 'Francia', 'Espania', "Belgica", "Polonia"]
nombre_completo = "Eduardo Gonzalez"

pais = input("Nombre de un pais europeo: ")

# in

# if pais in paises_europeos:
#     print(f"{pais} esta en el continente europeo")
# else:
#     print(f"{pais} no esta en el continente europeo")

# Salida = Entrada: Francia -> Francia esta en el continente europeo
#           Entrada: Mexico -> Mexico no esta en el continente europeo

# if "O" in nombre_completo:
#     print("Nombre contiene el caracter o")
# else:
#     print("Nombre no contiene el caracter o")

# not in

if pais not in paises_europeos:
    print("Pais no esta en el continente europeo")
else:
    print("Pais esta en el continente europeo")