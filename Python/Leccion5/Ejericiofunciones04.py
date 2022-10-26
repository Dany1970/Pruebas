# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:33:59 2022

@author: dania
"""

# Ejercicio 04: Calculadora de impuestos
# Definir una función para calcular el total de un pago incluyendo el IVA

def calc_impuestos(pago_sin_iva, iva):
    return pago_sin_iva + pago_sin_iva*iva/100

a_pagar = float(input('Ingrese el monto a pagar: '))

impuesto = float(input('Ingrese el impuesto: % '))

print(f'El monto total a pagar es $ {calc_impuestos(a_pagar,impuesto)}')
    