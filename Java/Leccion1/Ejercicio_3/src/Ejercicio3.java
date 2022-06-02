
import java.util.Scanner;

public class Ejercicio3 {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        //Ejercicio: área del rectángulo
//Se solicita calcular el área y el perímetro de un rectángulo para esto deberemos 
//crear las variables alto y ancho ambas de tipo int. El usuario debe proporcionar
//los valores de alto, ancho y luego imprimir el resultado, en el sgte formato
//(recuerden no usar acentos, respetar los espacios, mayúsculas, minúsculas y los 
//saltos de línea): Digite el alto del rectángulo. Digite el ancho del rectángulo
//. 

        System.out.println("Digite la altura del rectángulo: ");
        int alto = Integer.parseInt(entrada.nextLine());//o también podría usarse la inferencia de tipos
        System.out.println("Digite el ancho del rectángulo");
        int ancho = Integer.parseInt(entrada.nextLine());
        int area = alto * ancho;
        System.out.println("El área del rectángulo: " + area);
        int perimetro = 2 * alto + 2 * ancho;
        System.out.println("perimetro = " + perimetro);

    }
}
