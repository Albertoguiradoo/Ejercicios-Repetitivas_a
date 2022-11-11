'''
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó
10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un algoritmo
para determinar cuánto debe pagar mens
'''

meses = 20
contador= 0
mes1= 10
for i in range(1,meses+1):
    contador+=1
    mes1 = mes1*2
    print(f"el mes {contador} pagó {mes1}")
