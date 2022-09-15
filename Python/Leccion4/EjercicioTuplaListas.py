# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 18:40:42 2022

@author: Daniela Armijo
"""
import math

#Ejercicio: Dada la siguiente tupla:

# tupla = (13, 1, 8, 3, 2, 5, 8) #Definimos la tupla
# # Crear una lista que sólo incluya los menores a 5 e imprima por consola esos 
# # números

# listam = []
# for i in tupla:
#     if i < 5:
#         listam.append(i)

# print(listam)

# Usando la clase math, para lo cual hay que importarla (ver arriba)

numero = int(input('Ingrese un número: '))

while numero >= 0:
    
    print(f'La raíz cuadrada del número ingresado es {math.sqrt(numero): .2f}')# el 2f es para indicar los decimales
    
    numero = int(input('Ingrese un número: '))
    
print('El número ingresado es negativo')
 

