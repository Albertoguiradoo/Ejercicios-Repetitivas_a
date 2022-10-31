'''
Realizar una algoritmo que muestre la tabla de multiplicar de un número
introducido por teclado.
'''

num1 = 0
num1= int(input("Dime el númreo para realizar la tabla: \n"))

print(f"La tabla de {num1} es ")

for num in range (1,11):
   print(f"{num1} * {num} es: {num*num1}")
