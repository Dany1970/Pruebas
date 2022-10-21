# Ejercicio 9: Mostrar una frase sin espacios y contar su longitud
# Hacer un profeama donde el usuario ingrese una frase, se le 
# devolverá la misma frase pero sin espacios en blanco,
# y además e un contador de cuántos caracteres tiene la frase
# (sin contar los especios en blanco)
# Ejemplo: frase: vivir por siempre en paz
#frase final ) vivirporsiempreenpaz
# N° de caracterres 20

# frase = input('Ingrese una frase: ')
# frase = frase.replace(' ','')
# print(f'Frase final: {frase}')
# print(f'El número de caracteres sin contar espacios en blanco es {len(frase)}')
        
#Otra forma, con ciclos (creo que no hemos visto algunos métodos de los str)

otrafrase = input('Ingrese una frase: ')
frasesin = '' #Un str vacío para ir llenando
for caracter in otrafrase:
    if caracter != ' ':
        frasesin += caracter

print(f'Frase final: {frasesin}')
print(f'El número de caracteres sin contar espacios en blanco es {len(frasesin)}')
        
        
        
        