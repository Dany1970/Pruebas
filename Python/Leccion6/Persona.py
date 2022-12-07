# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 16:30:24 2022

@author: dania
"""

class Persona: #Creamos una clase
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): #método init dunder (double underscore)
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni #Con el guión bajo, se encapsula el atributo de una forma sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs
        
    def mostrar_detalle(self): # self es igual a this en Java
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni},{self.edad}, la dirección es: {self.args}, los datos importantes son: {self.kwargs}')
        
        
# persona1 = Persona('Juan','Zalazar', 22)    
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)

# persona2 = Persona('Daniela','Armijo', 52)
# print(f'objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} su edad es {persona2.edad}')

# #Tarea, lo mimso para la persona 1
# print(f'objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} su edad es {persona1.edad}')
# # Para agregar características o atributos a una clase necesitamos utilizar un mpetodo
# # que es el init, similar a un constructor 

# # los atributos de un objeto se pueden modificar? es como reutilizar una variable:
# # ekjemplo

# persona1.nombre = 'Viki'
# persona1.apellido = 'Lista'
# persona1.edad = 16

# print(f'objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} su edad es {persona1.edad}')

# #vemos que se ha modificado el objeto persona1

# # Los atributos son las características
# # Los métodos son el compportamoento que van a tener los objetos
# # Los métodos son como una función, pero dentro de una clase

# persona1.mostrar_detalle()
# persona2.mostrar_detalle()

# # Persona.mostrar_detalle() #Debemos pasarle una referencia para el self por ej
# Persona.mostrar_detalle(persona1) #aunque no es muy usado, no es eficaz, si se nos presenta un codigo así, hay que modificarlo

# persona1.telefono = '4445567'# Hemos creado un atributo (superficial) de un objeto

# print(f'Este es el teléfono de {persona1.nombre}: {persona1.telefono}')

# print(persona2.telefono) # da error porque no le hemos puesto un valor al atributo

persona3 = Persona('Rogelio', 'Romero', 20456789, 35, 'Teléfono','2345673','Calle Lopez', 567, 'manzana', 4, 'Casa', 5, altura = 180, peso = 90, color_favorito ='azul', auto = 'Toyota', modelo = 2021)
persona3.mostrar_detalle() #desde este método puede accederse a todos los atributos incluso los encapsulados
print(persona3._dni) # no deberíamos acceder de esta manera, dentro de las opciones del compilador 
                    # no aparece, pero como es sugerido, lo muestra. Esta forma de acceder a un atributo encapsulado
                    #demuestra DESCONOCIMIENTO del lenguaje
                
# No hay modificadores de acceso en Python, para hacerlo privado por ejemplo, se usa el _ como
# sugerencia para encapsular. Así debe entenderlo el programador (en JAVA tenemos modificadores de acceso
# public, private y protected)

# grabarse esto muy bien: _ es una sugerencia de encapsulamiento

# persona3.__atributoxx #el etributo está totalmente encapsulado
