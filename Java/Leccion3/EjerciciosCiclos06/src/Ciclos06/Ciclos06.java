/*Ejercicio 06: Pedir números hasta que se teclee un cero. Mostrar la suma de todos los 
números introducidos.


package Ciclos06;

import java.util.Scanner;


public class Ciclos06 {
    public static void main(String[] args) {
        int numero, suma = 0;
        Scanner entrada = new Scanner(System.in);
        System.out.println("El siguiente programa calculará la suma de los números "
                + "que ingrese, hasta que ingrese un 0");
        
        do{        
            System.out.println("Escriba un número: ");
     
           numero = Integer.parseInt(entrada.nextLine());
             suma += numero;        
        }while(numero != 0);{
         
                 
    }
        System.out.println("La suma de los números ingresados es " +suma);
    }
}
*/