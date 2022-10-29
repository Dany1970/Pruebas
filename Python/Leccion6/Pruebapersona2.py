# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 18:27:02 2022

@author: dania
"""
# Importando una clase creada para hacer objetos de esa clase
from Persona2 import Persona2
print('Creación de Objetos'.center(50, '-'))
if __name__ == '__main__':
    persona5 = Persona2('Seba', 'Lista', 35)
    persona5.mostrar_detalles()

    print(__name__)

print('Eliminación de Objetos'.center(50, '-'))
del persona5 #usamos el método destructor. No es tan común su uso
