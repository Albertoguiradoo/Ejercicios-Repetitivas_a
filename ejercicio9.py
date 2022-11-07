'''
Escribe un programa que dados dos números, uno real (base) y un entero
positivo (exponente), saque por pantalla el resultado de la potencia. No se puede
utilizar el operador de potencia.
'''

base = 0
exponente = 0
try:
    base = int(input("Dime la base: \n"))
    exponente = int(input("Dime el exponente: \n"))

    if exponente==0:
        print("1")  
    resultado = 1
    if exponente>0:
        
        for i in range(exponente):
            resultado *= base  
            
    print(f"La potencia de {base} elevado a {exponente} es ={resultado}")
except:
    print("El programa solo admite números. Por favor, intentelo de nuevo.")