'''
Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la
suma y la media de todos los números introducidos.
'''
num = 0
suma = 0
num = int(input("Dime un número: \n"))
contador = 0
media = 0
while num != 0:
    suma = suma + num  
    num = int(input("Dime un número: \n"))
    contador += 1
    media += 1

print(f"la suma total de los {contador} números es {suma}; y la media es {suma/media}")