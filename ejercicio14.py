'''
Una persona se encuentra en el kilómetro 70 de una carretera, otra se encuentra
en el km 150, los coches tienen sentido opuesto y tienen la misma velocidad.
Realizar un programa para determinar en qué kilómetro de esa carretera se
encontrarán.
'''

v1 = 70
v2 = 150

while v1!=v2:
    v1+=1
    v2-=1

print(f"Se encuentran en el kilómetro: {v1}")