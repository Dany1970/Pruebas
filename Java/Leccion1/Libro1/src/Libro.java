
import java.util.Scanner;

public class Libro {

    public static void main(String[] args) {

        Scanner consola = new Scanner(System.in);
        System.out.println("Proporcione el título de un libro: ");
        var titulo = consola.nextLine();
        System.out.println("Proporcione el autor del libro: ");
        var autor = consola.nextLine();
        System.out.println(titulo + " fue escrito por " + autor);

    }

}
