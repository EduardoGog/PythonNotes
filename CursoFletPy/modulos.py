# Teoría
# Un módulo podemos considerarlo como una librería de código
# Piezad de código
# Archivo que contiene funciones que queremos incluir en nuestra aplicación
# Estos archivos generalmente son llamados en otro archivo para poder
# hacer uso de las funciones declaradas

# Ejemplo

# banco.py
# usuarios = ["Jose", "Jorge", "Eduardo"]

# def registro_usuarios(nombre, id):
#     usuarios.append(nombre)
#     Agrega un usuario a la lista

# def borrrar_usuario(nombre):
#     usuarios.remove(nombre)
#     Borra un usuario segun el nombre proporcionado como parametro

# def total_usuarios():
#     return len(usuarios)
#     Regresa total de usuarios en la lista

# main.py
# import banco
# Palabra "import" ayuda a traer el archivo contenedor de las funciones

# print(banco.total_usuarios)
# Salida 3

# Se llama a total_usuarios como método para imprimir el total de
# usuarios en la lista