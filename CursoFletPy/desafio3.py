# Desafío 3
# Conversión de minutos a horas y minutos
minutos = float(input("¿Minutos a convertir a horas?: "))
# Conversion
horas = minutos // 60
mins = minutos % 60

#print(horas, "hrs", mins, "mins")

# Otra manera de imprimir
conversion = f"{horas} hrs con {mins} mins"
print(conversion)


