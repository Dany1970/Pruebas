
package test;

import domain.Persona;


public class TestArreglosObject {
    public static void main(String[] args) {
        Persona personas[] = new Persona[2];
        personas[0] = new Persona("Victoria");
        personas[1] = new Persona("Daniela");
        System.out.println("personas 0  = " + personas[0]);
        System.out.println("personas 1  = " + personas[1]);
    }
}
//Al ejecutar se muestra cada uno de los objetos el paquete con el operador de .
// la clase y la dirección de memoria de cada objeto
//Al agregar el método toString en la clase padre object, 
//se agrega el nombre y con el super.toString también muestra el espacio de memoria
//para entender esto tengo qeu mirar bien lo de herencia.
