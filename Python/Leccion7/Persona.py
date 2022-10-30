# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 23:06:20 2022

@author: dania
"""
class Persona: #Esta clase hereda de la clase Object
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
  
        
class Empleado(Persona): #Esta clase es hija de la clase persona
    def __init__(self, nombre, edad, sueldo): #se agregan los atributos heredados
        super().__init__(nombre, edad) # super es el constructor de la clase padre Objeto  
        self.sueldo = sueldo
        
empleado1 = Empleado('Ariel', 40, 75000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)

#Tarea: encapsular los atributos y agregar los métodos getters y setters
# crear otro objeto, pasar los datos para nombre, edad y sueldo 
# Mostrar esos datos luego modificarlos y mostrar nuevamente

