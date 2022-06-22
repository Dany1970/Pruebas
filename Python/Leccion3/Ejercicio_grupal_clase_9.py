# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 22:49:05 2022

@author: CODE_PEOPLE
"""
'''
Ejercicio 1: Diseñar un programa que, ingresado un año nos devuelva por consola si es un año bisiesto o no
Repetir la acción hasta que el usuario lo decida

# En el calendario gregoriano, un año normal consta de 365 días. Debido a que la 
# duración real de un año es en realidad 365.2425 días, un "año bisiesto" de 366 
# días se utiliza una vez cada cuatro años para eliminar el error causado por tres 
# años normales (pero cortos). Cualquier año divisible por 4 es un año bisiesto. 
# Hay un error de cáclulo sin embargo que debe tenerse en cuenta. Para eliminar 
# este error, el calendario gregoriano estipula que un año que es divisible por 
# 100 (por ejemplo, 1900) es un año bisiesto solo si también es divisible por 400.
# Por esta razón, los años siguientes no son años bisiestos: 1700, 1800, 1900, 2100,
# 2200, 2300, 2500, 2600 Esto se debe a que son divisibles por 100 pero no por 400.
# Los años siguientes son años bisiestos: 1600, 2000, 2400, Esto se debe a que son 
# divisibles por 100 y 400. Años para probar el código.

#Nota: el código sólo es válido para años posteriores a 400

anio = int( )

print('\n 1. Determine si el año ingresado es bisiesto \n 2. Salir del cálculo' )

opcion = int(input('Ingrese la opción según lo que desee hacer: '))

while opcion != 2:
    anio = int(input('Ingrese un año (posterior al 400): '))
    if anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0:
        print(f'El año {anio} es bisiesto')
        opcion = int(input('Ingrese la opción según lo que desee hacer: '))
    else:
        print(f'El año {anio} no es bisiesto')
        opcion = int(input('Ingrese la opción según lo que desee hacer: '))

if opcion == 2:
    print('Estás saliendo del cálculo. Vuelve pronto!')

  

    
Ejercicio 2: Calcular la suma de los "n" primeros números

        
nro = int(input('Ingrese un número: ')) 

print(f'Vamos a calcular la suma de los {nro} primeros números')   

cont = 0
suma = 0

while cont <= nro:
    suma = suma + cont
    cont += 1

print(f'La suma de los {nro} primeros números es {suma}')



















Ejercicio 3: leer 10 números e imprimir cuántos son positivos, cuántos negativos 
y cuántos ceros 




cuentaNros = 0
cuentaPositivos = 0
cuentaNegativos = 0

while cuentaNros < 10:
    diezNros = float(input(f'Ingrese el {cuentaNros+1}° número real: '))
    if diezNros > 0:
        cuentaPositivos += 1
    if diezNros < 0:
        cuentaNegativos += 1
    cuentaNros += 1
    continue
ceros = 10 - (cuentaPositivos + cuentaNegativos)
print(f'\n De los diez núneros ingresados: \n a) {cuentaPositivos} son positivos,\n\
b) {cuentaNegativos} son negativos y \n c) {ceros} son cero')

    
    
    
    
    
    
    
    
    
    
    
 
    
Ejercicio 4: suponga que se tiene un conjunto de calificaciones de un conjunto de 
10 alumnos, realizar un algoritmo para calcular el promedio y determinar la calificación más baja
'''

print('\nHola profe! Ingrese las calificaciones de sus alumnos')

cuentaNotas = 0
SumaNotas = 0
comparaNota = 10
while cuentaNotas < 10:
    nota = float(input(f'Ingrese la {cuentaNotas+1}° nota: '))
    cuentaNotas = cuentaNotas + 1
    SumaNotas = SumaNotas + nota
    if nota < comparaNota:
        minima = nota
        comparaNota = nota
    else:
        minima = comparaNota
    continue
promedio = SumaNotas/cuentaNotas
print(f'\nElpromedio de las notas es: {promedio} y la menor calificación es {minima}')         
  














