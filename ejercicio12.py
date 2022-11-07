'''
Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si
al final de cada mes deposita cantidades variables de dinero; además, se quiere
saber cuánto lleva ahorrado cada mes.
'''

mes= 0
total= 0
try:
    for i in range(1,13):
        mes=int(input("¿Cuánto has ahorrado este mes?: \n"))
        total+= mes
    print(f"Lo que has ahorrado en total este año es: {total}")

except:
    print("El programa solo admite números. Por favor, intentelo de nuevo.")

