# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 10:36:26 2022

@author: Daniela Armijo
"""

# Ejercicio 1: Iterar un rango de 0 a 10 e imprimir números divisobles entre 3

#Primero llenamos la lista con los números del 0 al 10:
#inicilizamos dos listas vacías: una va a contener todos los números y la otra sólo los divisibles por tres:
   
lista = [ ]
div3 = [ ]

for i in range(11):
    lista.append(i)

# ahora iteramos sobre la lista seleccionando los divisibles entre 3
    if i % 3 == 0:
        div3.append(i)

print(div3)    

# Resolución profe Ariel:

print('Rango de 0 a 10 con números divisibles entre 3')
for i in range(11):
    if i % 3 == 0:
        print(i, end=',') # el end se lo agregué yo.
    
# Ejercicio 2: crear un rango de 2 a 6 e imprímelos:
    
# Aprovecho la lista generada en el ej 1:
print('\nRango de 2 a 6')    #imprimí un salto antes del texto para que lo separe del print anterior
#es por si se ejecuta todo el código junto.

print(lista[2:7])

# Ejercicio 3: crear un rango de 3 a 10 pero con incremento de 2 en 2 en lugar de 1

print('Rango de 3 a 10 con paso 2')
for i in range(3,11,2):
    print(i, end = ',')
    
# OBSERVACIÓN: si corremos todo el código sin comentar los ejercicios anteriores, 
# puede hacer todos los prints jutos. Conviene imprimir algo entre medio, como hace el profe 
# (Y es lo que terminé haciendo)