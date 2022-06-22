# -*- coding: utf-8 -*-
"""
Created on Wed May 11 21:45:14 2022

@author: dania
"""

# En esta clase vamos a ver la sentencia if else

condicion = True

if condicion == True:
    print("Condición verdadera")
    
elif condicion == False:
    print("Condición Falsa")

else:
    print("Condición sin especificar")
    
#Vamos a usar el punto de ruptura, normalmente se pone en la línea de una variable
# Marcando un punto de quiebre se puede ver paso a paso la evolución del código
#Con debug (depurar) ... step (control f10). Probar poniendo a condición True, False y cualquier
#otra cosa

#Conversión de número a texto
'''
num = int(input("Ingrese un número en el rango de 1 a 3: "))

numTexto = ""

if num == 1 :
    numTexto = "número uno"

elif num == 2:
    numTexto = "número dos"

elif num ==3:
    numTexto = "número tres"
    
else:
    numTexto = "Has ingresado un número fuera de rango"

print(f'El numero ingresado es: {num} - {numTexto}')
'''

condicion = True
# if condicion:
#     print("Condición verdadera")
# else:
#     print("Condición falsa")

#De otra manera, con el operador ternario (para códigos cortos):

print("Condición verdadera") if condicion else print("Condición falsa")


    











