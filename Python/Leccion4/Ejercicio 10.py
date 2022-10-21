# Ejercicio 10: No repetir caracteres
# Hacer un programa que pida una cadena por teclado, luego 
# meter los caracteres en una lista sin repetir caracteres

chain = input('Ingrese una palabra: ')

lista = []
for i in chain:
    lista.append(i)

conjunto= set(lista)
sinrep = list(conjunto)
print(f'La lista de caracteres sin repetir de la palabra ingresada es: {sinrep}')


