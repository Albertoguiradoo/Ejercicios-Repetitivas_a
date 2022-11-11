'''
Una empresa les paga a sus empleados con base en las horas trabajadas en la
semana. Realice un algoritmo para determinar el sueldo semanal de N
trabajadores y, además, calcule cuánto pagó la empresa por los N empleados.
'''

trabajadores = 0
pagoHora = 0
dineroTotal= 0
horas = 0
contador= 0
dinero = 0

trabajadores= int(input("¿Cuántos trabajadores hay?: \n"))
pagoHora= int(input("¿Cuánto paga por hora?: \n"))


for num in range(1,trabajadores+1):
    contador += 1
    horas= int(input(f"Cuántas horas hizo el trabajador {contador} esta semana:\n "))
    dinero = pagoHora * horas
    print(f"El sueldo del trabajador {contador} es de: {dinero} ")
    dineroTotal+=dinero

print(f"El dinero total de los {contador} trabajadores es de : {dineroTotal}")


   