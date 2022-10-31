'''
Escribir un programa que imprima todos los números pares entre dos números
que se le pidan al usuario.
'''

vNum = []
num1 = 0
num2 = 0

num1= int(input("Dime el primer número: \n"))
num2= int(input("Dime el segundo número: \n"))

for num in range (num1,num2+1):
    if(num%2 == 0):
        print(f"El número {num} es par. ")
        vNum.append(num)#vNum.append es para guardar en lista.


print(vNum)
    
