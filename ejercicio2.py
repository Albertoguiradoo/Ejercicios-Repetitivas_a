'''
Crea una aplicación que permita adivinar un número. La aplicación genera un
número aleatorio del 1 al 100. A continuación va pidiendo números y va
respondiendo si el número a adivinar es mayor o menor que el introducido,a
demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El
programa termina cuando se acierta el número (además te dice en cuantos
intentos lo has acertado), si se llega al limite de intentos te muestra el número
que había generado
'''
import random

num = random.randint(1,100)
print (num)
num1 = 0
num1 = int(input("Dime le número haber si lo adivinas: \n"))

while num1 != num:
    print("número no adivinado. Por favor intentelo de nuevo.")
    num1 = int(input("Dime le número haber si lo adivinas: \n"))

print(f"has adivinado el número secreto que era: {num}")

