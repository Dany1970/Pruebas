# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 13:24:28 2022

@author: dania
"""

# Ejercicio 03: Función recursiva
# Imprimir números enteros desde cualquier número positivo de manera descendente hasta 1, usando
# funciones recursivas. Si se ingresa un núnero negativo no imprime nada

def descendente(nro):
    if nro >= 1:
        print(nro)
        return descendente(nro - 1)
    elif nro == 0:
        return
    elif nro <= 0:
        print('El valor ingresado es incorrecto')

#Tarea: que el número lo ingrese el usuario
number = int(input('Ingrese un número entero positivo: '))
print(descendente(number))
    

