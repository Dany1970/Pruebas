/*
Una clase es una plantilla que posee atributos y 
métodos. Un objeto es una instancia de una clase
 */
package Clases;

public class Persona {
    //Se recomienda primero definir los atributos
   String nombre;
   String apellido;
   
   //Métodos de la clase (Acciones)
   public void obtenerInformación(){
       System.out.println("Nombre: "+nombre);
       System.out.println("Apellido = " + apellido);
}
}
