# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 19:06:25 2022

@author: dania
"""

class Aritmetica:
    """
    El nombre de este tipo de comentario es : DocString, 
    esto es documentación de la clase en pthon
    Vamos a hacer algunas operaciones en esta clase, suma, resta, etc
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    
    #Método para sumar
    def sumar(self):
      return self.operandoA + self.operandoB
 
    def restar(self):
      return self.operandoA - self.operandoB

    def multiplicar(self):
      return self.operandoA * self.operandoB
    
    def dividir(self):
      return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(7, 9)
print(f'La suma de los números es: {aritmetica1.sumar()}')
print(f'La resta de los núneros es: {aritmetica1.restar()}')
print(f'La multiplicación de los núneros es: {aritmetica1.multiplicar()}')
print(f'La división de los núneros es: {aritmetica1.dividir():.2f}')
