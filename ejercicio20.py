'''
Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad
de números primos que queremos mostrar.
'''

vNUm =[]
cantidad= 0
primos= 0
cantidad= int(input("¿Cúantos números primos deseas que te muestre?:\n"))
contador  = 3

cantidad2 = cantidad 
def esPrimo(num):
    noPrimo= 0
    for i in range(2,num):
        if num%i==0:
            noPrimo +=  1 
    if noPrimo >= 1:
        return False
    else:
        return True

while cantidad!=0 :
    if esPrimo(contador)== True:
        vNUm.append(contador)
        cantidad-=1

    contador+=1 



print(f"Los {cantidad2} primeros números primos son :")
print(vNUm)