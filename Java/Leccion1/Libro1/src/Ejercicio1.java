//Tienda Libros: Ejercicio N° 1 - CODE_PEOPLE
import java.util.Scanner;

public class Ejercicio1 {
    
    public static void main(String[] args) {

        Scanner consola = new Scanner(System.in);
        System.out.println("Ingrese los siguientes datos del libro: ");
        System.out.println("Digite el nombre del libro: ");
        var tituloLibro = consola.nextLine();
        System.out.println("Proporcione el ID del libro: ");
        var nroid1 = consola.nextLine();
        System.out.println("Digite el precio del libro: ");
        var precio = consola.nextLine();
        System.out.println("Confirme si el envio es gratuito: ");
        boolean envioGratuito = Boolean.parseBoolean(consola.nextLine());
        
        System.out.println("El título del libro es: " +tituloLibro);
        System.out.println("El ID es: " +nroid1);
        System.out.println("Precio del libro: $ "+ precio);
        System.out.println("El envio del libro gratuito es : "+envioGratuito);

}}
