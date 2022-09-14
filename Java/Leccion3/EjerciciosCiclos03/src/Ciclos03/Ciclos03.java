/*
Ejercicio 3 : Leer números hasta que se introduzca un cero. Para cada uno
indicar si es par o impar. 
Primero con clase scanner
 */
package Ciclos03;

import java.util.Scanner;


public class Ciclos03 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un número: ");
        var numero = Integer.parseInt(entrada.nextLine());
        while(numero != 0) {
            if(numero % 2 == 0) {
                System.out.println("El número " +numero+ " es par");
            }
            else{
                System.out.println("El número " +numero+ " es impar");
            }
            System.out.println("Digite otro número: ");
            numero = Integer.parseInt(entrada.nextLine());
            

        }
        System.out.println("El número " +numero+ " finaliza el programa");
    }
    
    
}
