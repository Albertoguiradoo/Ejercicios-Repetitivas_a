'''
Escribe un programa que pida el limite inferior y superior de un intervalo. Si el
límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0.
Cuando termine el programa dará las siguientes informaciones:

-La suma de los números que están dentro del intervalo (intervalo abierto).
-Cuantos números están fuera del intervalo.
-He informa si hemos introducido algún número igual a los límites del intervalo.'''


lim_sup=0
lim_inf=0

lim_inf= int(input("Dime el límite inferior del intervalo: \n"))
lim_sup = int(input("Dime el límite superior del intervalo: \n"))

while (lim_sup<lim_inf):
    print("El intervalo superior es más pequeño que el inferior. El límite superior tiene que ser mayor que el inferior.")
    print("")
    lim_inf= int(input("Dime el límite inferior del intervalo: \n"))
    lim_sup = int(input("Dime el límite superior del intervalo: \n"))


#-La suma de los números que están dentro del intervalo (intervalo abierto).
numLista = 0
vNUm=[]

while (numLista != 0):
    numLista= int(input("Dime el número: \n"))

for num in range(lim_inf+1,lim_sup):
    print(f"la suma de los números dentro del intervalo es: {num}")
    