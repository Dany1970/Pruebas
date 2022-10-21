#Ejercicio 11: Hacer un programa que simule una agenda de contactos. Crear un diccionario 
# donde la clave sea el nombre del usuario y el valor sea el teléfono. El programa
# tendrá el siguiente menú de opciones:
    #1. Nuevo contacto
    #2. Borrar contacto
    #3. Ver contactos existentes
    #4. salir
    
agenda = {}

while True:
    print('\n 1. Nuevo contacto \n \
2. Borrar contacto \n \
3. Ver contactos existentes \n \
4. Salir' )

    o = int(input('Ingrese la opción según lo que desee hacer: '))

    if o == 1:
        nombre = input('Ingrese el nombre del contacto: ')
        telefono = input('Ingrese el número de teléfono: ')
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('Contacto agregado con éxito')
          
        else:
            print('El contacto ya existe')

    elif o == 2:
        nombre = input('¿Cuál es el nombre del contacto que desea borrar?: ')
        if nombre in agenda:
            del (agenda[nombre])
            print('Se ha borrado el contacto')
        else:
            print('El nombre no existe entre tus contactos')
        
    elif o == 3:
        print('Agenda de contactos')
        for clave, valor in agenda.items():
            print(f'Nombre {clave}, teléfono: {valor}')

    elif o == 4:
        print('Gracias por utilizar su agenda de contactos')
        break
    
    else:
        print('Se equivocó de opción de menú')
        print('\n')
    
    
        
        