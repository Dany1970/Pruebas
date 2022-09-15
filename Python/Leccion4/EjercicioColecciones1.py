# # Ejercicio 1: Eliminar duplicados de una lista
# # Escriba un programa para eliminar elementos duplicados de una lista
# # Mostrar en pantalla la lista sin duplicados

# # Versión con lista ingresada por el programador:
    
# lista1 = ['pepe', 2, 'cata', 3, 2, 2, 'pepe', True, True]

# #Para eliminar los elementos repetidos, transformamos la lista en set, que son 
# #colecciones sin elementos repetidos
# conjunto = set(lista1)

# #Volvemos a transformar el conjunto en lista
# lista2 = list(conjunto)
# print(f'La lista original es {lista1}')

# print(f'La lista sin elementos repetidos es {lista2}') 

# # Ejercicio 2: operaciones de conjuntos con listas
# # Escriba un programa que tenga dos listas y que a continuación cree las sgtes
# # listas (que no deben tener elementos repetidos)
# # Lista de palabras que aparecen en las listas
# # Lista de palabras que aparecen en la prmera lista pero no en la segunda
# # Lista de palabras que aparecen en la segunda lista pero no en la primera
# # Lista de palabras que aparecen en ambas listas

# # Voy a usar la lista del ejercicio anterior y una nueva

# lista3 = ['pepe','kato', 3, False, 1]

# lista4 = lista1+lista3
# conjunto1 = set(lista3)
# conjunto2 = conjunto - conjunto1
# conjunto3 = conjunto1 - conjunto
# conjunto4 = conjunto1 & conjunto
# print(f'Los elementos de ambas listas, sin repetir, son {list(conjunto1)}')        
# print(f'Los elementos que aparecen en la primera lista, pero no en la segunda, sin repetir, son {list(conjunto2)}')
# print(f'Los elementos que aparecen en la segunda lista, pero no en la primera, sin repetir, son {list(conjunto3)}')
# print(f'Los elementos que aparecen en ambas listas, sin repetir, son {list(conjunto4)}')   

# Ejercico 3: Ingresar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes personajes del Señor de lso ANilllos
# Nombre = Aragorn
# Clase = Guerrero
# Raza = Dúnedain del Norte

# Nombre = Gandalf
# Clase = Mago
# Raza = Istar

# Nombre = legolas
# Clase = Arquero
# Raza = Elfo Sindar

# hacemos un diccionario para cada personaje y luego armamos la lista:
Gandalf = {'Nombre' : 'Gandalf', 'Clase' : 'Mago', 'Raza': 'Istar'}
Aragorn = {'Nombre' : 'Aragorn', 'Clase' : 'Guerrero', 'Raza': 'Dúnadain del Norte'}
Legolas = {'Nombre' : 'Legolas', 'Clase' : 'Arquero', 'Raza': 'Elfo Sindar'}

# Inicializamos una lista vacía

personajes = [ ]

# llenamos con los diccionarios:

personajes.append(Gandalf)
personajes.append(Aragorn)
personajes.append(Legolas)

print(f'Los personajes principales de la Trilogía "El Señor de los Anillos", y sus características son {personajes}')