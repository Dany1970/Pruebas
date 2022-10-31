/*
Proyecto Caja: crearemos una clase para hacer cálculo de volúmenes de cajas.
*/
package caja;

public class Caja {//Creamos la clase
    int a;//definimos los atributos de la clase, que son las dimensiones de la caja
    int b;
    int c;
    
    public Caja(){//Método Constructor 1 (vacío)
        System.out.println("Se está ejecutando el constructor número uno");
    }
    
    public Caja(int a, int b, int c){//Constructor 2
       this.a = a;
       this.b = b;
       this.c = c;
        System.out.println("Se está ejecutando el constructor número dos");
               }
    //Vamos a crear método de esta clase que calculará el volumen de la caja 
    public void calcularVolumen(){
        int resultado = a * b * c;
            System.out.println("El volumnen de la caja es: " + resultado);
       
    // Quedó creada la clase con sus atributos y métodos
    // Crearemos ahora objetos con ella en otra java class
    }
   
}
