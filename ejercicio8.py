'''
Escribe un programa que pida el limite inferior y superior de un intervalo. Si el
límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0.
Cuando termine el programa dará las siguientes informaciones:

-La suma de los números que están dentro del intervalo (intervalo abierto).
-Cuantos números están fuera del intervalo.
-He informa si hemos introducido algún número igual a los límites del intervalo.'''

intervalo1_1 = 0
intervalo1_2 = 0
lim_sup=0
lim_inf=0



intervalo1_1= int(input("Dime el primer número: \n"))
intervalo1_2= int(input("Dime el segundo número: \n"))
print(f"El intervalo es {intervalo1_1,intervalo1_2}")

lim_inf= int(input("Dime el límite inferior del intervalo: \n"))
lim_sup = int(input("Dime el límite superior del intervalo: \n"))

while (lim_sup<lim_inf):
    lim_inf= int(input("Dime el límite inferior del intervalo: \n"))
    lim_sup = int(input("Dime el límite superior del intervalo: \n"))


#-La suma de los números que están dentro del intervalo (intervalo abierto).
numLista = 0
vNUm=[]


while (numLista != 0):
    numLista= int(input("Dime el número: \n"))

for num in range(intervalo1_1,intervalo1_2):
    print(f"la suma de los números dentro del intervalo es: {num}")
    vNUm.append(num)
