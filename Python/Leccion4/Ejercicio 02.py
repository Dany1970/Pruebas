# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:45:45 2022

@author: dania
"""

# Ejercicio 2: Modificar los elementos de una lista. Llenar una 
# lista con los números del 1 al 10, luego modificar los elementos de la lista 
# multiplicándolos por un valor ingresado por el ususario

lista = list(range(1,11))
tabla = int(input('¿Qué tabla de multiplicar desea que se le muestre?: '))
for i in lista:
    print(i, "|", tabla*i)
