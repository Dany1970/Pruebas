# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:41:55 2022

@author: dania
"""

# Ejercicio 2: Función con *args para multiplicar 
# Crear una función para multiplicar los valores recibidos de tipo numérico, 
# utilizando argumentos variables *args como parámetros de la función y regresar
# como resultado la multiplicación de todos los valores pasados como argumento

def producto(*args):
    resultado = 1;
    for n in args:
        resultado *= n
    return resultado

print(producto(2,10,3))
        
