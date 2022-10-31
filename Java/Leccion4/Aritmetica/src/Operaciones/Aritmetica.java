
package Operaciones;


public class Aritmetica {
    //Atributos de la clase
    int a;
    int b;
    //El constructor es un método especial. Cumple tres objetivos:
    // - Construye un objeto
    // - Reserva un espacio de memoria
    // - Inicializa los atributos de la clase
    public Aritmetica(){//Constructor 1 vacio
        System.out.println("Se está ejecutando el constructor número uno");
    }
    //Estamos viendo lo que se llama sobrecarga de constructores
    public Aritmetica(int a, int b){//Constructor 2
       this.a = a;
       this.b = b;
        System.out.println("Se está ejecutando el constructor número dos");
               }
    //Vamos a crear un método
    public void sumarNumeros(){
        int resultado = a + b;
            System.out.println("resultado = " + resultado);
    } 
    public int sumarConRetorno(){
        //int resultado = a + b;
        return this.a + this.b;
    }
    public int sumarConArgumentos(int a, int b){
        this.a = a;
        this.b = b;
        //return a + b;
        return this.sumarConRetorno(); //Llamando a otro método, en vez de usar el return anterior
        //Esto se puede hacer dentro de métodos que están en la misma clase
        
    }
            }
