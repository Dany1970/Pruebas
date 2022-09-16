# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 11:22:11 2022

@author: dania
"""

# Ejercicio 06 : Tabla de multiplicar
# hacer un programa ue pida un número por teclado y guarde
# en una lista su tabla de multiplicar hasta el 10. Por ejemplo:
# si digita el 5 la lista tendrá: 5, 10, 15, ..., 50

numero = int(input('Ingrese un número entero, para obtener su tabla de multiplicar: '))

tablan = [ ]

for i in range (11):
    tablan.append(numero*i)

print(tablan)    