# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 23:01:11 2022

@author: dania
"""
"""
Métodos getter y setter
El objetivo del encapsulamiento es que no se pueda acceder diretamente a los 
atributos de una clase, pero tenemos que tener un método para acceder a ellos y 
esos métodos son el getter (obtener)  y el setter (colocar, establecer, modificar) 
Para cada uno de los atributos, vamos a necesitar crear un método get y un método set
"""
class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        
    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido}, {self._edad} años')

    @property #decorador, se coloca en cada método
    def nombre(self): #Método getter
        print('Estamos utilizando el método get')
        return self._nombre
    @property
    def apellido(self):
        return self._apellido
    @property
    def edad(self):
        return self._edad
    
        
    @nombre.setter #esto también se coloca en cada método
    def nombre(self, nombre): #Método setter
        print('Estamos utilizando el método set')
        self._nombre = nombre
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    @edad.setter
    def edad(self, edad):
        self._edad = edad
    
    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self.edad}')
   
#Comprobación del método principal en ejecución:

# Si hacemos un código de prueba dentro de la misma clase        
# para que no se ejecute este código cuando usemos la clase en otro archivo
if __name__ == '__main__':
        
    persona1 = Persona2('Daniela', 'Armijo', 52)
    #persona1._nombre #Ojo, esto es lo que NO HAY QUE HACER
    print(persona1.nombre) #Llamamos al método getter, que no necesita que le enviemos parámetros
    print(persona1.apellido)   
    print(persona1.edad)
    
    #Ahora llamamos al método setter
    
    persona1.nombre = "Jorge Alberto"
    print(persona1.nombre)
    print(persona1.mostrar_detalles())
    
    #Si un atributo no tiene el método set para ser modificado, es un atributo read-only (de sólo lectura)
    #Igualmente debe tener el método get para poder obtenerlo, mostrarlo
    
    
    # persona1.mascota = "perro"
    # print(persona1.mascota)
    
    #Tarea crear tres objetos más, utilizando los métodos getter y setter 
    # para modificar y mostrar los cambios
    
    persona2 = Persona2("name", 'surname', 00)
    persona2.nombre = 'Victoria'
    persona2.apellido = 'Lista'
    persona2.edad = 16
    print(persona2.mostrar_detalles())
    
    persona3 = Persona2("name", 'surname', 00)
    persona3.nombre = 'Caleste'
    persona3.apellido = 'Fernández'
    persona3.edad = 37
    print(persona3.mostrar_detalles())
    
    persona4 = Persona2("name", 'surname', 00)
    persona4.nombre = 'Mercedes'
    persona4.apellido = 'Gómez'
    persona4.edad = 42
    print(persona4.mostrar_detalles())
    
    print(__name__)