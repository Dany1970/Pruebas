
package Clases;


public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1;
        persona1 = new Persona(); //Llamamos al constructor
        persona1.nombre = "Daniela";
        persona1.apellido = "Armijo";
        persona1.obtenerInformación(); //Llamando al método
        
        Persona persona2 = new Persona();
        System.out.println("persona2 = " +persona2);
        System.out.println("persona1 = " + persona1);
        persona2.obtenerInformación();
        persona2.nombre = "Jorge";
        persona2.apellido = "Lista";
        persona2.obtenerInformación();
    }
}
