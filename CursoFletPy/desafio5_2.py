# import desafio5
# Mi solución
from desafio5 import conversation
import random
#from desafio5 import conversation
# print("Bienvenido al proyecto de Chatbot")
# print("Hola soy un ChatBot...")
# input("")
# respuestas = conversation
# aleatoria = random.choice(conversation)
# print(aleatoria)

# Solución Philip
# Paso 1 Imprimir la bienvenida al ChatBot
print("Bienvenido a mi primer programa chatbot en pyhton!")
# Paso 2 Saludar al usuario
print("Hola soy un ChatBot...")
# Paso 3 Esperar respuesta de usuario
respuesta_user = input()
# Paso 4 Responder al usuario   
respuesta_bot = random.choice(conversation)
# comparar respuesta de usuario con respuesta de chatbot
if respuesta_user.lower() == respuesta_bot.lower():
    respuesta_alternativa = random.choice(conversation)
    print(respuesta_alternativa)
else:
    print(respuesta_bot)
# Paso 5 terminar programa