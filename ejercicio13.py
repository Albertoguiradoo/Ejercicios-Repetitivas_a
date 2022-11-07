'''
Una empresa tiene el registro de las horas que trabaja diariamente un empleado
durante la semana (seis días) y requiere determinar el total de éstas, así como el
sueldo que recibirá por las horas trabajadas.
'''
dineroHora = 0
horasAldía= 0
totalHoras= 0
contadorDías= 0
try: 
    dineroHora = int(input("¿Cuánto dinero gana a la hora?: \n"))

    for i in range(1,7):
        contadorDías += 1
        horasAldía = int(input(f"¿Cuántas horas has trabajado el día {contadorDías}?: \n"))
        totalHoras+= horasAldía
    print(f"La suma total de horas trabajadas es de {totalHoras}")
    print(f"El sueldo de la semana es de {totalHoras*dineroHora} euros")
except:
    print("El programa solo admite números. Por favor, intentelo de nuevo.")

