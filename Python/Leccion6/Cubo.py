# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 19:52:02 2022

@author: dania
"""

class Cubo: #creamos la clase
    """
    Crear una clase llamada Cubo, debe tener tres atributos, altura, ancho y profundidad
    el nombre del método será calcular_volumen. Los datos deben ser ingresados 
    por el usuario
    """
    # Con el método init dunder, le asignamos los atributos a la clase
    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad

    # creamos un método para la clase:
        
    def calcular_volumen(self):
        return self.altura * self.ancho * self.profundidad

# Instaciamos la clase
# Objeto 1
an = float(input('Ingrese el ancho del prisma: '))
h = float(input('Ingrese la altura del prisma: '))
prof = float(input('Ingrese la profundidad del prisma: '))

prisma = Cubo(an, h, prof)
print(f'El volumen del prisma es {prisma.calcular_volumen()}')








