
package Operaciones;


public class Aritmetica {
    //Atributos de la clase
    int a;
    int b;
    //El constructor es un método especial
    public Aritmetica(){//Constructor 1
        System.out.println("Se está ejecutando el constructor número uno");
    }
    
    public Aritmetica(int a, int b){//Constructor 2
       this.a = a;
       this.b = b;
        System.out.println("\"Se está ejecutando el constructor número dos");
               }
    //Vamos a crear un método
    public void sumarNumeros(){
        int resultado = a + b;
            System.out.println("resultado = " + resultado);
    } 
    
            }
