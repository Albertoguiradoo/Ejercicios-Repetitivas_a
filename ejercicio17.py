'''
Una empresa les paga a sus empleados con base en las horas trabajadas en la
semana. Para esto, se registran los días que trabajó y las horas de cada día.
Realice un algoritmo para determinar el sueldo semanal de N trabajadores y
además calcule cuánto pagó la empresa por los N empleados.
'''


trabajadores = 0
pagoHora = 0
día = 0
dineroTotal= 0
horasDía = 0
contador= 0
dinero = 0
contador2= 0

trabajadores= int(input("¿Cuántos trabajadores hay?: \n"))
pagoHora= int(input("¿Cuánto paga por hora?: \n"))
día= int(input("¿Cuánto dias trabajó esta semana?: \n"))

for num in range(1,trabajadores+1):
    contador += 1
    for i in range(1,día+1):
        
        horasDía= int(input(f"Cuántas horas hizo el trabajador {contador} el día{}:\n "))
    