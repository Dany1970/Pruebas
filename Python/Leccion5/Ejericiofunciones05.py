# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:43:23 2022

@author: dania
"""

# Ejercicio 05: Convertidor de temperaturas
# Hacer dos funciones para pasar de °F a °C y viceversa

def celsius_a_fahrenheit(celsius):
    
    return celsius * 9/5 + 32

def fahrenheit_a_celsius(fahrenheit):
    
    return (fahrenheit - 32) * 5/9

while True:
    print('\t MENÚ \n \
1. Convertir °C a °F \n \
2. Convertir °F a °C \n \
3. Salir' )

    opcion = int(input('Seleccione la conversión que desea hacer: '))

    if opcion == 1:
        temp1 = float(input('Ingrese una temperatura en °C: '))
        print(f'\n La temperatura {temp1} °C ccorresponde a {celsius_a_fahrenheit(temp1)} °F \n')

    elif opcion == 2:
        temp2 = float(input('Ingrese una temperatura en °F: '))
        print(f'\n La temperatura {temp2} °F corresponde a {fahrenheit_a_celsius(temp2)} °C \n')

    elif opcion == 3:
        print('Gracias por usar el convertidor de escalas de temperatura')
        break
    
    else:
        print('Ha ingresado una opción no válida. Intente nuevamente')

