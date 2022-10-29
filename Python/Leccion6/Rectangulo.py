# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 19:31:02 2022

@author: dania
"""

class Rectangulo: #creamos la clase
    """
    Crear una clase llamada Rectangulo, debe tener dos atributos, altura y base
    el nombre del método será calcular_area. La base y la altura deben ser ingresados 
    por el usuario y los objetos deben ser tres
    """
    # Con el método init dunder, le asignamos los atributos a la clase
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    # creamos un método para la clase:
        
    def calcular_area(self):
        return self.altura * self.base

# Instaciamos la clase con 3 objetos:
# Objeto 1
b1 = float(input('Ingrese la base del rectángulo: '))
h1 = float(input('Ingrese la altura del rectángulo: '))

rectangulo1 = Rectangulo(b1, h1)
print(f'El área del rectángulo es {rectangulo1.calcular_area()}')

#Objeto 2
b2 = float(input('Ingrese la base del rectángulo: '))
h2 = float(input('Ingrese la altura del rectángulo: '))

rectangulo2 = Rectangulo(b2, h2)
print(f'El área del rectángulo es {rectangulo2.calcular_area()}')

#Objeto 3
b3 = float(input('Ingrese la base del rectángulo: '))
h3 = float(input('Ingrese la altura del rectángulo: '))

rectangulo3 = Rectangulo(b3, h3)
print(f'El área del rectángulo es {rectangulo3.calcular_area()}')            