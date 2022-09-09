//Ejercicio 1: Leer un númmero y mostrar su cuadrado, repetir 
// el proceso hasta que se introduzca un número negativo
package Ciclos01;

import java.util.Scanner;


public class Ciclos01 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        int numero, cuadrado; //Definimos las variables a usar
        System.out.println("Digite un número: "); //Solicitamos al usuario que ingrese un número
        numero = Integer.parseInt(entrada.nextLine()); //Esto no me queda muy claro
        while(numero >= 0) { //Acá se inicia el ciclo
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El número " +numero+ "elevado al cuadrado es:" +cuadrado);
            System.out.println("Digite otro número: ");
            numero = Integer.parseInt(entrada.nextLine());
            
        }
        System.out.println("El programa ha finalizado por ingresar un número negativo");
                
    }
    
}
