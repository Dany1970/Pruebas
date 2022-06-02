# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 21:36:24 2022

@author: dania
"""

#Este primer ejercicio es para mostrar que las variables son dinámicas y pueden ir 
#cambiando, incluso aunque sean de distinto tipo.

'''
miVariable = 3
print(miVariable)   #acá mivariable es de tipo entera

miVariable = "a"  #Acá es la misma variable, ahora tipo string. Cambia, es dinámica
                    # pero además, cambia el tipo, y no es necesario especificarlo
                    #por eso es dinámicamente tipado.
print(miVariable)

miVariable = 3.5
print(miVariable) #La palabra reservada print con los paréntesis es una función
                  #e imprime lo que ponemos entre paréntesis en la consola
# Hemos visto en este ejercicio asignación de variables, reutilización de variables
# y la función print, para # imprima en la consola lo que aparece entre paréntesis.
  
            

#las variables asigna un valor en un lugar de la memoria, cada una de estas 
#"casillas" es una posición única

x = 10

y = 2

z = x + y

print(z)


# Lugar de memoria donde está guardado el valor de una variable

#Para saber el lugar de memoria donde están asignadas estas "literales" tenemos
#la dirección id

print(id(x)) #la función id muestra ese lugar

#Las literales se escriben x512 (siempre x y los tres últimos dígitos de la id
#- son valores hexadecimales) Pero si volvemos a ejecutar, el valor cambia. 
#La memoria es volátil. Cuando el programa finaliza, se borran todas las 
#casillas. Al correrlo nuevamente, ocupa otro lugar

#A este número x512 se le llama referencia de memoria o simplemente referencia


#Los archivos en Git nunca se deben manipular
# Acá me perdí algo que dio Natalia (buscar)
#para que quede todo "cometeado"

#Tipos de datos

a = "hola alumnos"

#Una función dentro de otra, en este caso imprimir en consola el tipo de dato que tiene
#nuestra variable
print(a)
print(type(a))

#Las variables en Python son dinámicas, pueden cambiar el tipo de dato
#igualmente se puede poner como pista el tipo de dato, como una referencia, pero esto no es necesario

b = str(4)
print(b)
print(type(b))

#para ingresar una variable de tipo flotante, se pone el número con punto flotante
c = 23.4
print(c)
print(type(c)) #al imprimir vemos que es de tipo float

#Tipos booleanos

d = True #usar mayúscula para True
print(d)
print(type(d))#al imprimir vemos que es bool

#Al ser Python orientado a objetos, los tipos de datos son clases, es por eso que al 
# mostrar el tipo dice class

# Tipos int, float, string, bool
 
x = 10
print(x)
print(type(x)) 
x = 14.5
print(x)
print(type(x))
x = "Hola alumnos"
print(x)
print(type(x))
x = False
print(x)
print(type(x))
x = True
print(x)
print(type(x))

# Manejo de cadenas

miGrupoFavorito = "Queen"
print(miGrupoFavorito)

# Vamos a concatenar con el símbolo +
# como estamos usando cadenas, (no números) lo usa para concatenar

print("Mi grupo favorito es " +miGrupoFavorito)

#También se puede concatenar dentro de la asignación de la variable.
# Ejemplo: concatenando dos cadenas on un espacio (el espacio también se concatena)
    
myFavoriteGroup = "Metallica" + " "  +"The Best Heavy Metal Band"
print("Mi grupo favorito es " +myFavoriteGroup)

#Al ser cadenas adyacentes, también puden concatenarse sin el +. Ejemplo:

mismascotas = "Kato " "Bigotes"
print(mismascotas)

# por supuesto que esto último también podría hacerse con un solo juego de 
# comillas

# Otro ejemplo para concatenar

Materia = "Fisica"
caracteristica = "de primero"

print("Mi materia favorita es: ", Materia, caracteristica)  

# Vamos a crear otras variables

numero1 = "7"
numero2 = "8"
print(numero1 + numero2)

#Al ser las variables cadenas, el operador + concatena, no suma

#Para que las pueda sumar, debo transformarla al tipo entero

print(int(numero1)+int(numero2))

#Importante: una palabra no lo puede pasar a tipo entero, por ej si en vez de poner 7 
# ponemos siete, no lo puede concatenar, ni sumar


# Tipos booleanos

miBooleano = True
print(miBooleano)

miBooleano2 = 1 > 2
print(miBooleano2)

miBooleano3 = 3 > 2
print(miBooleano3)

#Ahora vamos a usar un If (condicional)

if miBooleano3:
    print("el resultado es verdadero")
else:
    print("el resultado es falso")

if miBooleano2:
    print("el resultado es Verdadero")
else:
    print("el resultado es falso")

# Ingreso de datos por el usuario

#Hasta ahora, le hemos asignado nosotros los valores a las variables (código duro)
#Si queremos que los ingrese el usuario usamos la función input:

    #Función input 
    
resultado = input("Ingrese un número: ") # la función input recibe cualquier tipo
                                        # de dato y regresa un dato tipo string 
print(resultado) 

# Conversión de la entrada de datos (a tipo entero)

variable1 = int(input("Escribe el primer núnero: ")) # Convierte al str en tipo entero
variable2 = int(input("Escribe el segundo númnero: ")) #idem
suma = variable1 + variable2
print("El resultado de la suma es: ", suma) #Así sale la suma, de otra manera
#si no lo transformamos a tipo entero, el + concatena



operandoa = 8
operandob = 5
suma = operandoa + operandob
print("El resultado de la suma es ", suma)

# Otra forma: con la f de format: para imprimir varias líneas o valores de variables
#Fornato de interpolación, para incluir variables en una cadena, usando la f y las llaves
# entonces no hace falta concatenar. Es la forma preferida por los programadores

print(f'El resultado de la suma es {suma}')

resta = operandoa - operandob

print(f'El resultado de la resta es {resta}')

producto = operandoa * operandob

print(f'El resultado del producto es {producto}')

cociente = operandoa / operandob

print(f'El resultado de la división es {cociente}')

cociente1 = operandoa // operandob

print(f'El resultado de la división entera es {cociente1}')

modulo = operandoa % operandob

print(f'El resto de la división es {modulo}')

potencia = operandoa ** operandob

print(f'La potencia es {potencia}')

#Calcular el área y el perímetro de un rectángulo

alto = int(input("Ingrese el alto del rectángulo: "))
ancho = int(input("Ingresa el ancho del rectángulo: "))                 

area = alto * ancho

perimetro = (alto + ancho ) * 2
print("\n")
print(f"El área del rectángulo es {area} ")
print("\n")
print(f"El perímetro del rectángulo es {perimetro}")

#Asignación y reasignación de variables, con sintaxis reducida

miVariable3 = 10 + 1 #Si no le pongo el +1, imprime 10, si se lo pongo, reasigna
                    # a la variable el valor 11
print(miVariable3)

#Otra sintaxis para hacer lo mismo

miVariable3 += 1
print(miVariable3) #Ahora suma uno más, imprime 12

#Esta sintaxis funciona con todos los operadores

miVariable3 -= 2
print(miVariable3)

miVariable3 *= 3
print(miVariable3)

miVariable3 /= 2
print(miVariable3) #Notar que al dividir, lo transforma en float


#Operadores con cadenas: concatenación

texto = "ho" + "la"
print(texto)

texto1 = 'hola mundo ' * 4

print(texto1)

#Comparación

d = 4
b = 2

comparando = d == b #mirar el doble signo == para el igual en esta expresión

print(comparando)

comparando1 = d > b

print(comparando1)

comparando2 = d != b

print(comparando2)

#Otros operadores de comparación son <= y >= 
# Esto operadores son la base de muchos algoritmos que vamos a usar, así es que
#a practicar!


#Ejercicio: es par o impar

numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print(f"El número {numero} es par")
else:
    print (f"El número {numero} es impar")

#Ejercicio: determinar si es mayor de edad

edad = int(input("¿Cuántos años tienes?: "))

if edad >= 18:
    print(f"Tu edad es {edad} por lo tanto eres mayor de edad")
else:
    print(f'Tu edad es {edad} por lo tanto eres menor de edad')
     
#Operadores lógicos
#OPeradores binarios and y or
#Operador and
a = False #Le asignamos con código duro

b = True #idem

resultado = a and b

print (resultado)

#Operador or
resultado2 = a or b

print(resultado2)

#Ejercitamos cambiando los valores de a y b para ver los resultados

#Operador not (unario)

print (not a)


#Ejercicio : valor dentro de un rago

nro = int(input("Ingrese un número: "))
 
salida = nro <=5 and nro >= 0

#print ("¿El número ingresado está en el intervalo [0, 5]?", salida)

print(f'¿El número ingresado está en el intervalo? {salida}')
'''
'''
# Ejercicio con operador or
# Un padre puede asistir al juego de su hijo
# 1) verificamos si tiene vacaciones
# 2) Verificamos si tiene horas libres
# 3) 

vacaciones = False
diadescanso = False
 
if vacaciones or diadescanso:
    print("El padre puede asistir al juego de su hijo")
else: 
    print("Tiene trabajo que hacer")


Ejercicio
Preguntar la edad al usuario

Si la edad está dentro de los 20 o los 40 años, está dentro del rango
Combinar operadores and y or

edad = int(input("Ingrese su edad:"))

if edad >=20 and edad < 30 or edad >=30 and edad <40:
    print("Su edad está dentro del rango")
else:
    print("Su edad no está dentro del rango")


Ejercicio
Solicitar al usuario dos valores determinar cuál es el mayor

numero1 = int(input("Ingrese un número:"))
numero2 = int(input("Ingrese otro número:"))

if numero1 > numero2:
    print("El número mayor es: ", numero1)
else:
    print("El mayor número es: ", numero2)
'''
'''
Ejercicio Tienda de libros
Mostrar: Ingrese los datos del libro
Digite el nombre del libro
Digite el ID del libro
Digite el precio del libro
Indicar si el envio es gratuito (T/F)
Mostrar:
Nombre:
ID:
Precio
Envio Gratuito o no?


print("Ingrese los siguientes datos del libro")
titulo = input("Escriba el título del libro: ")
nroid = int(input("Digite el ID del libro: "))
precio = float(input("Digite el precio del libro: "))

if precio >= 1500:
   envioGratuito = True
else:
   envioGratuito = False

# print(f'''
      # Título : {titulo}
      # ID : {nroid}
      # Precio : {precio}
      # Envío Gratuito: {envioGratuito}
      # ''')

#Este formato es para la visualización con las tabulaciones    

