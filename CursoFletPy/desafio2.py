# Desafío 2. if - else, if - elif
# Juego - jugado / suspendido /
# Jugado = cuantos goles anotados por el quipo local?
# 4
# Cuantos goles anotados por el quipo vistante?
# 3
# Salida = Equipo local gano el partido


status = input("¿Cual es el estado del partido?: ")
if status == "jugado":
    local = int(input("¿Cuantos goles anoto el equipo local?: "))
    visitante = int(input("¿Cuantos goles anoto el equipo visitante?: "))
    if local > visitante:
        print("Gano equipo local")
    elif local < visitante:
        print("Gano equipo visitante")
    else:
        print("Juego empatado")
elif status == "suspendido":
    print("Juego suspendido")
else:
    print("Estado invalido")