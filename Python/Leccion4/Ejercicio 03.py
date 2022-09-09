# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 22:06:14 2022

@author: dania
"""
# FUNCION SORT

# Ejercicio 3: Insertar elementos y ordenarlos
# Pedir números y meterlos en una lista, cuando el ususario introduzca el número
# 0, nuestro programa dejaría de insertar. Por último mostrar los números ordenados 
# de menor a mayor

lista = [ ]
salir = False # estamos creando una "bandera"

while not salir:
    numero = int(input('Digite un número:'))
    
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
    
    lista.sort()

print('\nLa lista ordenada es en forma creciente es: ', lista)

    
