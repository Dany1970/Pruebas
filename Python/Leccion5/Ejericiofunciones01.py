# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 08:51:01 2022

@author: dania
"""

# Ejercicio 01: Crear una función para sumar los valores de tipo numéricos recibidos
# utilizando arguemntos variables *args como parámetros de la función y egregar como
# resutado la suma de los valores pasados como argumentos.

def suma(*args):
    resultado = 0
    for n in args:
        resultado += n
    return resultado    
        
print(suma(1,2,3))