# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 09:12:29 2022

@author: dania
"""

# Ejercicio 04 : sumar números pares dentro  de un rango
# hacer un programa para sumar números pares dentro de un rango
# Por ej: rango de 2 a 30, suma = 240

suma = 0
for i in range(31):
    if i % 2 != 0:
        continue
    else:
        suma += i

print(f'La suma de los pares dentro del rango es {suma}')

