'''
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de
números a introducir). El programa debe informar de cuantos números
introducidos son mayores que 0, menores que 0 e iguales a 0.
'''

num = 0
contadorMayor = 0
contadorMenor = 0
contadorIgual = 0
num= int(input("Dime cúantos números deseas introducir: \n "))

for num in range (0,num):
    num=int(input("Dime el  número: \n"))
    if num > 0:
        contadorMayor += 1
        
    elif num< 0:
        contadorMenor += 1
    else:
        contadorIgual += 1
        

print(f"hay {contadorMayor} números que son mayores que 0.")        
print(f"hay {contadorMenor} números que son menores que 0.")
print(f"hay {contadorIgual} números que son igual que 0.")