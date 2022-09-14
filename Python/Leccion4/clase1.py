# # -*- coding: utf-8 -*-
# """
# Created on Tue Aug 16 19:33:07 2022

# @author: dania
# """
# #CLASE 1     16/08/2022
# # COLECCIONES EN PYTHON

# # LISTAS

# lista = ['pipi','jorge','dani','kato'] #Para las listas se usan CORCHETES
# # Imprimir la lista completa
# print(lista)
# # imprimir sólo el primer elemento (el elemento cero)
# print(lista[0])
# # imprimir el último elemento
# print(lista[-1])

# #Recuperar un rango de la lista
# print(lista[0:2]) # va desde el elemento 0 hasta el 1

# print(lista[ :3]) #Imprime los tres primeros elementos

# print(lista[1: ]) #imprime desde el elemento ubicado en la posición 1, que es el segundo NO ONLVIDAR

# #Modificar un valor dentro de la lista

# lista[3]='zeus'
# print(lista)

# #Iterar una lista: mediante un ciclo for, podemos, por ejemplo, imprimir toda la lista
# for nombre in lista:
#     print(nombre)
# else:
#     print("se acabaron los elementos de la lista")
    
# #Ver cuántos elementos tiene una lista: función len
# print(len(lista))

# #El operador de punto nos permite acceder a diferentes métodos para trabajar, por ej, con una lista
# # La función para insertar un nuevo elememto a la lista es append
# lista.append('Dike')
# print(lista)

# Agregamos en el final de la Clase 2: 
# Una lista puede tener distintos tipos de datos: str, otra lista, float, int, booleano...
# Vamos a agregar un elemento de cada tipo para que se visualice esto.
# Usamos para ello la fucnión append

# lista.append([1,2,3])
# lista.append(3.14)
# lista.append(4)
# lista.append(True)

# print(lista)
    
# #Insertar un elemento en un lugar cualquiera
# lista.insert(1,'Bigotes')
# print(lista)

# #Eliminar un elemento de la lista
# lista.remove('zeus')
# print(lista)

# #Eliminar el último elemento de la lista
# lista.pop() #Por defecto elimina el último
# print(lista)

# #Para eliminar un índice específico
# del lista[1]
# print(lista)

# #Eliminar borrar o limiar toda la lista
# lista.clear()
# print(lista) #Aparecen los corchetes vacíos

# #Eliminar la lista
# del lista
# #print(lista) #Nos da un error de nombre, como que no está definido

# # Verificamos cómo trabajar día a día en git
# # Si cuando deseamos comitear, nos damos cuenta que estamos en una rama diferente de la master,
# #vamos a tener que volver atrás con los cambios que hemos hecho en nuestro archivo, para poder volver a 
# #la rama master. Nos conviene cortar el código que hayamos escrito y pegarlo en un archivo de 
# #texto, luego volver a git y resetear (ver video en Clase 1 de Colecciones, antes de Tuplas)
# # Una vez que hemos podido cambiarnos a la rama master, volvemos a copiar el código en el archivo,
# # guardamos y ya podemos comitear en la rama que deseemos.
 

# #TUPLAS

# #Otro tipo de colecciones son las TUPLAS, que son listas INMUTABLES)
# cocina = ('cuchillo', 'tenedor', 'cuchara') # las tuplas se encriben entre CORCHETES
# print(cocina)
# print(len(cocina))# Imprime el tamaño de la tupla


# #Cómo acceder a un elemento de la tupla
# print(cocina[0]) #nos muestra el primer índice, que es el 0
# print(cocina[-1])

# #Cómo acceder a un rango de la tupla

# print(cocina[0:1])

# verduras = ('papa') #parece una tuple pero no, es tipo string
#                     #Debe llevar una coma al final para ser tupla

# verdura = ('papa',) #Acá si es tupla

# print(cocina[0:2])

# #Recorremos los elementos de la tupla:

# for elemento in cocina:
#     print(elemento, end = ' ')# El print por defecto usa \n para final de línea. Si queremos
#                                 #cambiarlo, se pone end = 'el final de linea deseado'
# #Para hacer cambios en una tupla, primero hay que convertir a lista y luego volver a tupla
# #aunque esto no es una buena práctica (no sé por qué?)
# cocinaLista = list(cocina)
# cocinaLista[0] = 'plato'
# cocina = tuple(cocinaLista)
# print('\n',cocina)

# #Eliminar una tupla
# del (cocina)
# #print(cocina)   
     


# #TIPO SET EN PYTHON

# #Listas: mantienen un orden y se pueden mutar
# #Tuplas: Mantienen un orden y no se puedne mutar
# #Set: no tienen orden, es decir no tiene índice, tampoco puede tener duplicacdos.
# # No son completamente mutables ni inmutables ya que se  puede agregar o eliminar elementos

# planetas = {'Marte','Júpiter', 'Venus'}
# print(len(planetas))

# #Revisar si un elemento existe (o no) dentro de un set

# print('Martes' in planetas)
# print('Júpiter' not in planetas)

# planetas.add('Tierra')
# print(planetas)
# # si lo volviese a agrrgear, no se repite
# planetas.add('Marte')

# print(planetas)

# # Aquí la gran importancia de los sets, cuando necesitamos que no aparez<can elementos duplicado
# # como puede ser un DNI, una patente

# # Eliminar elementos, puede arrojar un error si el elemento no está

# planetas.remove('Tierra')
# print(planetas)

# #Tener presente indicar correctamente el elemento a eliminar para que no de error

# # Otra función similar: discard
# planetas.discard('jupiter')
# print(planetas)

# # la diferencia entre remove y discard es que si nos equivocamos al escribir el elemento con remove, da error
# # y se detiene la ejecución del código. Esro no pasa con discard

# # Limpiar set
# planetas.clear()
# print(planetas)

# #Eliminar set
# del planetas
# #print(planetas) #da error de nombre
# #Falta la clase 2

# DICCIONARIOS
# Un diccionario está compuesto por dos elementos: UNA CLAVE Y UN VALOR
# Se usan llaves para armarlos

# diccionario = {
#     'IDE': 'Integrated Development Environment',
#     'OOP': 'Objected Oriented Programming',
#     'SABD': 'Sistema de Administración de Base de datos'}

# print(diccionario)

# print(len(diccionario))#imprime el tamaño del diccionario

# #Acceder a un diccionario con la llave(key)

# print(diccionario['IDE'])

# #Otra forma de recuperar un elemento

# print(diccionario.get('OOP'))

# print(diccionario.get('SABD'))

# #Modificar elementos de un diccionario
# diccionario['IDE'] = 'Entorno de desarrollo integrado'
# print(diccionario)

# # Cómo recorrer los elementos
# # Para que muestre las claves:
    
# for termino in diccionario:
#     print(termino)

# # para acceder al valor, necesitamos una función: item

# for termino, valor in diccionario.items():
#     print(termino, valor)

# # Otras maneras de acceder a un diccionario
# #similar a la primera forma, para acceder a la clave:
    
# for termino in diccionario.keys():
#     print(termino) #recorre sólo las llaves

# #Para acceder sólo al valor:
# for valor in diccionario.values():
#     print(valor)    
    
# # Comprobar la existencia de algún elemento:
# print('IDE' in diccionario)    
 
# # Agregar un elemento:

# diccionario['PK'] = 'Primary key'
# print(diccionario)

# #Eliminar un elemento
# diccionario.pop('SABD')
# print(diccionario)

# # Vaciar un diccionario
# diccionario.clear()
# print(diccionario)

# #Eliminar un diccionario

# del diccionario # el diccionario se borró

# Otras cuestiones relacionadas con LISTAS
#Concatenamos Listas

lista1 = [1,2,3,1]
lista2 = [4,5,6,1]
lista3 = lista1+lista2
print(lista3)

# Para agregar varios elementos en una lista 
#usamos EXTEND
lista3.extend([7,8,9,1])
print(lista3)

#Función para ubicar en qué índice está el valor ingresado
print(lista3.index(5))
# print(lista3.index(0)) daría error porque 0 no está en la lista

# Cómo saber cúantos elementos iguales tiene una lista
print(lista3.count(1))

#Para invertir la lista
lista3.reverse()
print(lista3)

#Para que una lista se multiplique repitiendo sus elementos:}
lista3 = lista3 * 2
print(lista3)

#Métodos de ordenamiento
#Con la función sort 
lista3.sort()
print(lista3)

#de mayor a menor

lista3.sort(reverse = True)
print(lista3)

# Repaso de tuplas

tupla = (4, 'Hola', 9.7, {1,2,3}, 4, 'Hola')
print(tupla)

#algunas funciones que se pueden usar con las tuplas

print(4 in tupla) # Acción booleana, su respuesta es de tipo
                    #booleana
# Lo que podemos usar dentro de tuplas son: index, count, len 
# las tupplas se pueden convertir a listas y viceversa


#Repaso del tipo set o conjunto

#Para definir un conjunto
# conjunto = set()#Conjunto vacío, es una forma de inicializar un conjunto para agregarle elementos
# conjunto1 = {'bye'}#Otra forma de inicializar un conjunto es con llaves y poniendo un elemento
#             #después se pueden agregar más
# conjunto.add(2)#Añadimos elementos
# conjunto.add('martes')
# print(conjunto)
# conjunto1.add('hola')
# print(conjunto1)

# print(3 not in conjunto1) #preguntamos si un elelmento pertenece a un conjunto
# #Igualdada de conjuntos
# print(conjunto == conjunto1)

# #Operaciones entre conjuntos (poner ejemplos más entretenidos)
# #Union
# conjunto3 = conjunto | conjunto1
# print(conjunto3)

# #Intersección
# conjunto4 = conjunto & conjunto1
# print(conjunto4) #la salida set() indica conjunto vacío

# #Diferencia
# conjunto5 = conjunto - conjunto1
# print(conjunto5)

# #Diferencia simétrica

# conjunto6 = conjunto ^ conjunto1
# print(conjunto6) 

# #Es subconjunto?
# print(conjunto1.issubset(conjunto3))

# #Incluye a?
# print(conjunto3.issuperset(conjunto1))

# #El disjunto?
# print(conjunto3.isdisjoint(conjunto1))

# #Convertir un conjunto totalmente en inmutable
# conjunto1 = frozenset #no se pueden agregar ni eliminar ni cambiar elementos al conjunto

# # Diccionarios
# diccionarioNuevo = {'Azul':'Blue', 'Rojo' : 'Red','Negro':'Black','Blanco':'White','Amarillo':'Yellow'}
# print(diccionarioNuevo)
# #Cómo eliminar

# del (diccionarioNuevo['Azul'])
# print(diccionarioNuevo)

# #Los diccionarios pueden almacenar diferentes tipos de datos (cadenas, float, int, listas)

# diccionario2 = {'Ariel':{'Edad':40,'Altura':1.83},'Osvaldo':[45,1.85],'Natalia':[35,1.67]}
# print(diccionario2)

#Ejercicio: Ingresar elementos al diccionario seleccionArgentina:
# Armé un diccionario un poco diferente con otros datos de los jugadores que econtré en Wikipedia.
# seleccionArgentina = {
#     10:{'Nombre':'Lionel Messi','Edad':35,'Goles':86,'Equipo':'PSG', 'Posición': 'Delantero'},
#     11:{'Nombre':'Ángel Di María','Edad':34,'Goles':25,'Equipo':'Juventus', 'Posición': 'Delantero'},
#     21:{'Nombre':'Paulo Dybala','Edad':28,'Goles':3,'Equipo':'AS Roma', 'Posición': 'Delantero'},
#     19:{'Nombre':'Nicolás Otamendi','Edad':34,'Goles':4,'Equipo':'Benfica', 'Posición': 'Defensor'},
#     1:{'Nombre':'Franco Armani','Edad':35,'Goles':0,'Equipo':'River Plate', 'Posición': 'Arquero'},
#     13:{'Nombre':'Cristian Romero','Edad':24,'Goles':0,'Equipo':'Tottenham', 'Posición': 'Defensor'},
#     8:{'Nombre':'Marcos Acuña','Edad':30,'Goles':0,'Equipo':'Sevilla', 'Posición': 'Defensor'},
#     3:{'Nombre':'Nicolás Tagliafico','Edad':30,'Goles':0,'Equipo':'Olympique', 'Posición': 'Delfensor'},
#     23:{'Nombre':'Emiliano Martínez','Edad':29,'Goles':0,'Equipo':'Aston Villa', 'Posición': 'Arquero'},
#         }
# print(seleccionArgentina)
# print(seleccionArgentina[21])

# #Vamos a recorrer el diccionario

# for llave in seleccionArgentina:
#     print(llave)

# for llave, valor in seleccionArgentina.items():
#     print(llave, valor)

# print(f'Tenemos cargados en el diccionario la cantidad de {len(seleccionArgentina)} jugadores')

# SETIEMBRE
# Método con listas llamado PILAS

pila = [1, 2, 3] #Ingresamos una lista
#Si hacemos una pila, ponemos una cosa arriba de otra, no podemos sacar nada más que el último imgresado
#Agregamos elemento
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
elementoBorrado = pila.pop() #Elimina el último elemento de nuestra lista
print('Sacamos el elemento', elementoBorrado, 'y ahora la pila quedó así', pila)

# Método de listas llamado colas

# Estructuras de datos de tipo fifo (fisrt input/fisrtOutput)
cola = ['Dani', 'Jorge']
cola.append('Viki')
cola.append('Kato')
print(cola)

#Ahora sacamos elementos

seRetira = cola.pop(0)
print(f'Atendido el cliente {seRetira}, quedan en la cola {cola}')

seRetira = cola.pop(0)
print(f'Atendido el cliente {seRetira}, quedan en la cola {cola}')

seRetira = cola.pop(0)
print(f'Atendido el cliente {seRetira}, quedan en la cola {cola}')

seRetira = cola.pop(0)
print(f'Atendido el cliente {seRetira}, quedan en la cola {cola}')








