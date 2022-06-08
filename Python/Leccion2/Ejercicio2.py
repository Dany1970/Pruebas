# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 10:08:43 2022

@author: dania
"""

# Determinar la solución lógica de la siguiente operación.

# ((3 + 5 x 8 ) < 3 and ((- 6/3 x 4 ) + 2 < 2)) or ( a > b)

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))

op1 = 3 + 5 * 8
op2 = -6/3 *4 + 2

if op1 < 3 and op2 < 2 or a > b:
    print('El resultado de la operación es Verdadero') 
else:
    print('El resultado de la operación es falso')                