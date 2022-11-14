'''
Realizar un ejemplo de menú, donde podemos escoger las distintas opciones
hasta que seleccionamos la opción de “Salir”.
'''


def menú():
    opciones= ""
    while opciones!="Salir":
        print("Escribe: Calendario para ver cuando son los partidos del mundial")
        print("Escribe: Goles para ver todos los goles del mundial")
        print("Escribe: Jugadores para ver todos los jugadores de cada equipo")
        print("Escribe: Donde para saber en que estadio es cada partido")
        print("Escribe: Salir para salir del ménu")
        try:
            opciones=str(input("Dimer una opción: \n"))
        except:
            print("El programa solo admite letras. Por favor, intentelo de nuevo.")
    print("Has salido del menú.")

opciones = menú() 