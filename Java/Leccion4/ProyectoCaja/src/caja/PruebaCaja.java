/*
Proyecto Caja: Esta clase de Prueba, usará la clase creada Caja para crear dos 
objetos
*/
package caja;


public class PruebaCaja {
    public static void main(String[] args) {//llamamos al método main
        int a = 10;//Inicializamos las variables para usar el Constructor vacío
        int b = 7;
        int c = 3;
        
        //OBJETO 1
        Caja caja1 = new Caja();//Creamos un objeto con los parámetros (o argumentos?)
                                
        caja1.a = 3;
        caja1.b = 1;
        caja1.c = 2;
        
        caja1.calcularVolumen();//Usamos el método para calcular el volumen 
        
        //OBJETO 2
        Caja caja2 = new Caja(4, 5, 1); //Usamos el constructor 2 para crear otro objeto
        System.out.println("ancho = " + caja2.a);
        System.out.println("profundidad = " + caja2.b);
        System.out.println("alto = " + caja2.c);
        
        caja2.calcularVolumen();//mismo método para calcular el volumen de este objeto
    }
}
