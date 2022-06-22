# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 19:02:25 2022

@author: dania
"""

'''Haremos un programa que cuando el usuario ingrese su edad
le diga, o imprima, la etapa de su vida en una breve oración 
0-10 la infancia es increible y bella
10-19 tienes muchos cambios mucho que estudiar
20 a 29 amor y comienza el trabajo
30 a 50 tenés hijos y los ves crecer
50 a 70 vienen los nietos y la jubilación
70 en adelante recta final

'''
edad = int(input('Ingrese su edad: '))

if edad >= 0 and edad <=10:
    print("estás en la infancia, esta etapa es increible y bella")

elif edad > 10 and edad <=19:
    print("en esta etapa vendrán los cambios, hay que estudiar mucho")

elif edad >= 20 and edad <=29:
    print("en esta etapa llega el amor; comienza el trabajo")

elif edad >=30 and edad <=49:
    print("tenés hijos y los ves crecer")

elif edad >=50 and edad <= 70:
    print("vienen los nietos, la última etapa de trabajo")
 
elif edad > 70:
    print("a disfrutar lo construido")