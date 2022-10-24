'''
Crea una aplicación que pida un número y calcule su factorial (El factorial de un
número es el producto de todos los enteros entre 1 y el propio número y se
representa por el número seguido de un signo de exclamación. Por ejemplo 5! =
1x2x3x4x5=120),
'''


resultado= 1
num = 0
num = int(input("Dime el número para calcular el factorial: \n"))

for numero in range(1,num+1):
    resultado = resultado  * (numero)
    
print(f"El factorial de {num} es: {resultado}")

