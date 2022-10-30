'''
Algoritmo que pida caracteres e imprima 
‘VOCAL’ si son vocales y
‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un espacio.
'''

letra= ""

while letra!= " ":
    letra= str(input("Dime la letra: \n"))
    if (letra =="a")or (letra =="e") or (letra =="i") or (letra =="o") or (letra =="u"):
        print("la letra es una VOCAL.")
    else:
        print("la letra es NO VOCAL.")
    
print("El programa ha terminado.")
