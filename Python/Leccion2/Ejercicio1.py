# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 08:49:34 2022

@author: dania
"""

#Ejercicio 1
'''
Escribir la siguiente expresión algorítmica:
    a3 * (b2 - 2ac)/2b
1) pedimos al usuario 3 valores. a,b,c
2) mostramos el resultado final
'''
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

calculo = a**3*(b**2 - 2*a*c)/(2*b)

print(f'El resultado final es {calculo}')