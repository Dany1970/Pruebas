# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 09:17:59 2022

@author: dania
"""

# Ejercicio 05: Factorial del un número positivo
# Hacer un programa para calcular el factorial de un número positivo

numero = int(input('Ingrese un número entero positivo: '))

while numero <= 0:
    
    print('El número ingresado no es positivo')
        
    numero = int(input('Ingrese otro número: '))
    
factorial = 1
for i in range(2,numero+1):
    factorial *= i

print(f'El factorial del número {numero} es {factorial}')
