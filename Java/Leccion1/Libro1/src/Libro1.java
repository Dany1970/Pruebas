/*
        Ejercicio: Tienda de libros
Mostrar: Ingrese los siguientes datos del libro
Digite el nombre del libro
Digite el ID del libro
Digite el precio del libro
Indicar si el envío es gratuito (True/False)
Mostrar:
	Nombre:
	ID: 
	Precio:
	Envío Gratuito?:
*/
import java.util.Scanner;

public class Libro1 {

    public static void main(String[] args) {

        Scanner consola = new Scanner(System.in);
        System.out.println("Ingrese los siguientes datos del libro: ");
        var titulo = consola.nextLine();
        System.out.println("Proporcione el ID del libro: ");
        var nroid = consola.nextLine();
        System.out.println("Digite el precio del libro: ");
        var precio = consola.nextLine();
        System.out.println("Confirme si el envio es gratuito: ");
        boolean envioGratuito = Boolean.parseBoolean(consola.nextLine());
        
        System.out.println(titulo +" #"+nroid );
        System.out.println("Preciodel libro: $"+ precio);
        System.out.println("El envio del libro gratuito es : "+envioGratuito);

    }

}
