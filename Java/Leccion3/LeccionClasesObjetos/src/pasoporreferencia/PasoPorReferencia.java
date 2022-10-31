//Paso por Referencia
package pasoporreferencia;

import Clases.Persona;


public class PasoPorReferencia {

    private static Object persona3;
    public static void main(String[] args) {
        //Vamos a usar la clase Persona, hay que importarla porque está dentro de otro paquete
            Persona persona3 = new Persona();
            persona3.nombre = "Ester";
            cambiarValor(persona3);
      System.out.println("El cambio que hicimos en el nombre es: "+persona3.nombre);
      persona3 = cambiarElValor(persona3);
      Persona persona4 = new Persona();
      persona4 = cambiarElValor(persona4);
        System.out.println("El nuevo valor del objeto es; "+persona4.nombre);
    }

public static void cambiarValor(Persona persona){//Paso por referencia
    persona.nombre = "Maria";
    }       
public static Persona cambiarElValor(Persona persona){//un método de tipo Object desde la clase persona
    if(persona == null){
        System.out.println("Valor de persona es inválido: null");
        return null;
    }
    else{
    persona.nombre = "Mónica";
    return persona;
        
}
}
}
