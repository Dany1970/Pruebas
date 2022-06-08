# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 10:31:42 2022

@author: dania
"""

# Ejercicio 4: Área y longitud de un circulo
# Hacer un programa para ingresar el radio de un circulo y se reporte su área y la longitud de la circunferencia.

# Área = Pi * r2
# Longitud = 2 * Pi * r
# En este ejercicio vamos a necesitar importar el modulo math porque tiene el valor de Pi
# Se escribe:   import math

import math

r = float(input('Ingrese el radio del círculo: '))

print('Vamos a calcular el área del círculo: ')

area = math.pi*r**2
if r < 0:
    print("Ha ingresado un valor incorrecto para el radio")

else:
    print(f"El área del círculo es: {area}")


    
    
 
