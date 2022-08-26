# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 19:33:07 2022

@author: dania
"""
#cLASE 1     16/08/2022
# COLECCIONES EN PYTHON

lista=['pipi','jorge','dani','kato']
# Imprimir la lista completa
print(lista)
# imprimir sólo el primer elemento (el elemento cero)
print(lista[0])
# imprimir el último elemento
print(lista[-1])

#Recuperar un rango de la lista
print(lista[0:2]) # va desde el elemento 0 hasta el 1

print(lista[ :3]) #Imprime los tres primeros elemetnos

print(lista[1: ]) #imprime desde el elemento un¿bicado en la posición 1, que es el segundo NO ONLVIDAR

#Modificar un valor dentro de la lista

lista[3]='zeus'
print(lista)

#Iterar una lista
for nombre in lista:
    print(nombre)
else:
    print("se acabaron los elementos de la lista")