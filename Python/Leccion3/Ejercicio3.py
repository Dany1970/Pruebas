# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 10:47:46 2022

@author: dania
"""

#Calcular estación del año
#Pedir al usuario que ingrese un mes del año, el valor debe ser entre 1 y 12
#Luego le decimos en qué estación del año está
#Vernao 21/12 al 21/3
#Otoño 21/3 al 21/6
#Invierno 21/6 al 21/9
#Primavera 21/9 al 21/12

#Agregado: le voy a pedir el día también

dia = int(input('Ingrese el día del mes (El valor estará comprendido entre 1 y 31): '))
mes = int(input("Ingrese un mes del año (el valor debe ser entre 1 y 12): "))

if (mes == 12 and dia >= 21 and dia <= 31) or (mes == 1 and dia >= 1 and dia <= 
31) or (mes == 2 and dia >= 1 and dia <= 29) or (mes == 3 and dia >= 1 and dia < 21):
    print("Estás en verano")

elif (mes == 3 and dia >= 21 and dia <= 31) or (mes == 4 and dia >= 1 and dia <= 
30) or (mes == 5 and dia >= 1 and dia <= 31) or (mes == 6 and dia >= 1 and dia < 21):
    print("Estás en otoño")
    
elif (mes == 6 and dia >= 21 and dia <= 30) or (mes == 7 and dia >= 1 and dia <= 
31) or (mes == 8 and dia >= 1 and dia <= 31) or (mes == 9 and dia >= 1 and dia < 21):
    print("Estás en invierno")
    
elif (mes == 9 and dia >= 21 and dia <= 30) or (mes == 10 and dia >= 1 and dia <= 
31) or (mes == 11 and dia >= 1 and dia <= 30) or (mes == 12 and dia >= 1 and dia < 21):
    print("Estás en primavera")

else:
    print("los números ingresados no corresponden a un mes o a un día")
    