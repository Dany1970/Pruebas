# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 18:40:42 2022

@author: Daniela Armijo
"""

#Ejercicio: Dada la siguiente tupla:

tupla = (13, 1, 8, 3, 2, 5, 8) #Definimos la tupla
# Crear una lista que sólo incluya los menores a 5 e imprima por consola esos 
# números

listam = []
for i in tupla:
    if i < 5:
        listam.append(i)

print(listam)
