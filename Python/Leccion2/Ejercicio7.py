# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 19:16:22 2022

@author: dania
"""

'''
Sistema de calificaciones
El objetivo del programa será crear un sistema de calificaciones
de la siguiente manera: le pedimos al usuario que ingrese un valor
del 0 al 10. Si se ingresa 9 a 10, imprime A, 8  y menor a 9, B, 
7 y menor a 8 C, 6 y menor a 7, D
0 y menor a 6 F
De lo contrario, el valor ingresado es incorrecto
  
'''
nota = float(input("Ingrese la nota de su examen: ")) 


if nota >= 9 and nota <= 10:
    print("A")


elif nota >= 8 and nota < 9:
    print("B")
    

elif nota >= 7 and nota < 8:
    print("C")
    

elif nota >= 6 and nota < 7:
    print("D")

elif nota >= 0 and nota < 6:
    print("F")

else:
    print("El valor ingresado no corresponde a una nota")

