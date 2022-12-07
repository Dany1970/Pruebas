package Operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        int a = 10;//variables locales
        int b = 7;
        miMetodo();
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 1;
        aritmetica1.sumarNumeros();
        
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("resultado usando argumentos = "+resultado);
        
        System.out.println("aritmetica1 a: "+aritmetica1.a);
        System.out.println("aritmetica1 b: "+aritmetica1.b);
                
        Aritmetica aritmetica2 = new Aritmetica(5, 8);
        System.out.println("aritmetica2 = " + aritmetica2.a);
        System.out.println("aritmetica2 = " + aritmetica2.b);
        //aritmetica1 = null; nunca utilizar esto, no se debe hacer
        //System.gc(); garbage collector; método para limpiar residuos, es pesado, no usar
        Persona persona = new Persona("María", "García"); //No hay que importar nada porque estamos
        System.out.println("persona = " + persona);       //trabajando dentro de la misma plantilla donde
        System.out.println("Persona nombre: "+persona.nombre);//está definida la clase
        System.out.println("Persona apellido: "+persona.apellido);
                                                                       
                
    }
  public static void miMetodo(){
      int a = 10;
      System.out.println("Aquí hay otro método");
  }  
}
/*Podemos crear otra clase dentro de una clase, pero no puede ser de tipo 
público, por defecto va a ser default o package, no hace falta ponerlo porque 
es por defecto*/
class Persona{
    String nombre;
    String apellido;
    
Persona(String nombre, String apellido){//Método Constructor
    super(); //Método cnstructor de la clase padre
    new Imprimir().imprimir(this);
    this.nombre = nombre;               //Tampoco se le asigna el tipo porque por defecto
    this.apellido = apellido;           //Es default o package
    System.out.println("Objeto persona usando this: "+this);
    
}
        
                    
    
 }
class Imprimir{
    public Imprimir(){
        super(); //El constructor de la clase padre, para reservar memoria
    }

    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: " +persona);
        System.out.println("Impresión del objeto actual(this) "+this);
}
}