# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 12:42:43 2022

@author: dania
"""

# Ejercicio 7: Juego adivina el número
# Se debe generar un número aleatorio entre 1 y 100, y luego ir pidiendo números indicando
# es mayor, es menor, según sea mayor o menor con respecto a N. El proceso termina cuando
# el usuario acierta y allí se debe mostrar el número de aciertos

import random

print('\nAdivine un número en la menor cantidad de aciertos!')
numero_usuario = int(input('Ingrese un número entero entre 1 y 100: '))

numero_azar = random.randint(1, 101)

contM = 0
contm = 0
while numero_usuario != numero_azar:
    
    if numero_usuario > numero_azar:
        print('El número que ha ingresado es mayor.')
        numero_usuario = int(input('Ingrese un número menor al anterior: '))
        contM += 1
        
    else:
        print('El número que ha ingresado es menor.')
        numero_usuario = int(input('Ingrese un número mayor al anterior: '))
        contm += 1
        
print(f'\nExcelente! El número que debía adivinar era {numero_azar}. Ha adivinado el número después de {contM+contm+1} intentos')