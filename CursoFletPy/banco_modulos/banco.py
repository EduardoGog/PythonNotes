usuarios = ["Jose", "Jorge", "Eduardo"]

def registro_usuarios(nombre, id):
    usuarios.append(nombre)
    # Agrega un usuario a la lista

def borrrar_usuario(nombre):
    usuarios.remove(nombre)
    # Borra un usuario segun el nombre proporcionado como parametro

def total_usuarios():
    return len(usuarios)
    # Regresa total de usuarios en la lista
