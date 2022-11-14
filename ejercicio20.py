'''
Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad
de números primos que queremos mostrar.
'''

vNUm =[]
cantidad= 0
primos= 0
cantidad= int(input("¿Cúantos números primos deseas que te muestre?:\n"))
noprimo = 0
vNum= ()
try:
        num = int(input("Dime un numero: \n"))
        for i in range(2,num):
            if num%i==0:
                noPrimo +=  1 
        if noPrimo >= 1:
            print("El número no es primo")
        else:
            print("El número es primo")
except:
    print("El programa solo admite números. Por favor, intentelo de nuevo.")

def vNum():
    
    print(f"Los {cantidad} números primos son : {primos}")




vNUm(1,cantidad+1)