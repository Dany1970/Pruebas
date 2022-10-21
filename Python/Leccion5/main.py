# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 11:02:09 2022

@author: dania
"""
# Comenzamos con funciones

# def saludo_manana(): # No se puede llamar antes de definirla
#     print('Buenos días profesor')

# saludo_manana() # Estamos llamando a la función

# saludo_manana() #la podemos llamar n veces

#  Desempaquetado de listas o list unpacking
# "Extraemos y mostramos" los elementos de una lista, tupla o diccionario, definiendo una función: 

# def mostrar(name, lastname):
#     print(name + ' ' + lastname)

# person = ['viki', 'lista']

# mostrar(person[0], person[1])
# mostrar(*person)

# #También se aplica a tuplas y diccionarios
# person2 = ('Jorge', 'Lista')
 
# mostrar(*person2)

# person3 = {'lastname': 'Armijo', 'name' : 'Daniela'}

# mostrar(**person3) #Acá van dos asteriscos, porque son dos cosas: clave y valor

# Repaso ciclo for else

# numbers = [1, 2, 3, 4, 5] #probar con la lista vacía, igual se ejecuta el else

# for n in numbers :
#     print(n)
#     # if n ==3:
#     #     break # con estas dos líneas no se ejecuta el else
# else:
#     print('Esto se terminó')

# Listas por comprensión (sin utilizar un for)

# names = ['Dani', 'Jorge', 'Viki', 'Kato']

# alongD = [p for p in names if p[0] == 'D']
# print(alongD)

#También se puede hacer con diccionarios, arrays, tuplas

# bottleC = [{'name': 'Quilmes','country': 'Arg'},
#            {'name': 'Corono','country': 'Mx'},
#            {'name': 'Stella','country': 'Belgium'}]

# Arg = [b for b in bottleC if b['country'] == 'Arg']

# print(Arg)
# print(bottleC)

# Paso de argumentos

# def mi_funcion(name, lastName): #Pasamos los parámetros (son las variables)
#     print('Saludos a todos los que se unen a través del canal de YouTube')
#     print(f'Nombre : {name}, Apellido : {lastName}')

# mi_funcion('Jorge','Lista') #los argumentos son los valores que toma la variable (parámetro)
# mi_funcion('Dani', 'Armijo')
# mi_funcion('Viki', 'Lista')

# La palabra return en funciones
# Creamos una función para sumar

# def sumar(a, b):
#     return a + b

# resultado = sumar(30, 70)

# print(f'El resultado de la suma es {resultado}')
# # o directamente:

# print(f'El resultado es {sumar(40,50)}')

# Valores por default. Para evitar errores en el código, pueden asignarse valores por 
# default dentro de la función

# definimos una función exactamente igual a la anterior:
# def sumar2(a = 0, b = 0): #probar antes sin valores, luego le asiganmos los valores
#     return a + b

# resultado = sumar2() #Si no le hemos puesto valores pro defalt esto da error
# # TypeError: sumar2() missing 2 required positional arguments: 'a' and 'b'

# print(f'El resultado de la suma es {resultado}')
# print(f'El resultado es {sumar2(40,50)}')#si pongo otros argumentos, los cambia automáticamente

# Argumentos (variables) en funciones

# def listarNombres(*nombres): #el argumento es una tupla (no modificable) 
#                              #Pero no sabemos cuántos nombres serán ingresados,
#                              #ponemos entonces el* para indicar eso
#                              #la sintaxis más común es *args
#     for nombre in nombres:
#         print(nombre)
        
# #Ahora usamos la función, ingresando una lista de nombres con código duro

# listarNombres('Dani','Jorge','Viki','Kato')

        














