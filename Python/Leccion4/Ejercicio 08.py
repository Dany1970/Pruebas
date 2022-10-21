# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 15:06:52 2022

@author: dania
"""
# Ejercicio 08: Menú interactivo - cajero automático
# hacer un programa que simule un cajero automático con un saldo inicial de $ 1000
# y tendrá el siguiente menú de opciones
# Ingresar dinero en la cuenta
# Retirar dinero de la cuenta
# Mostrar dinero disponible
# Salir

saldo = 1000
print('\n 1. Ingresar dinero en la cuenta \n \
2. Retirar dinero de la cuenta \n \
3. Mostrar dinero disponible \n \
4. Salir' )

o = int(input('Ingrese la opción según la operación que desee hacer: '))

if o != 1234:
        print('Ingresó una opción incorrecta')
        o = int(input('Ingrese otra opción: '))
        
while o != 4:
    if o == 1:
        ingreso = float(input("¿Cuánto dinero va a ingresar?: $ "))
        saldo += ingreso
        o = int(input('Ingrese otra opción: '))
    
    elif o == 2:
        retiro = float(input("¿Cuánto dinero va a retirar?: $ "))
        if retiro <= saldo:
            saldo -= retiro
            o = int(input('Ingrese otra opción: '))
        else:
            print(f'El saldo de su cuenta es $ {saldo}. Si desea retirar, Ingrese un \
monto menor o igual a $ {saldo}: ')

    elif o == 3:
        print(f'Saldo disponible = $ {saldo}')
        o = int(input('Ingrese otra opción: '))
    
   
print('Gracias por utilizar nuestros servicios')    
  

        
        