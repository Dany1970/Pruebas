//Paso por Referencia
package pasoporreferencia;

import Clases.Persona;


public class PasoPorReferencia {

    private static Object persona4;
    public static void main(String[] args) {
        //Vamos a usar la clase Persona, hay que importarla porque está dentro de otro paquete
            Persona persona1 = new Persona();
            persona4.nombre = "Ester";
            cambiarValor(persona4)
      ystem.out.println("El cambio que hicimos en el nombre es: "+persona4);
    }

public static void cambiarValor(Persona persona){//Paso por referencia
    persona.nombre = "Maria";
    }       
}
