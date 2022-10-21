/*
Ejercicio 07: Pedir números hasta que se introduzca un número negativo y calcular
la media. Usando el método Scanner
 */
package Ciclos07;

import java.util.Scanner;

public class Ciclos07 {
    public static void main(String[] args) {
       int numero, suma = 0, contador = 0;
        Scanner entrada = new Scanner(System.in);
        System.out.println("El siguiente programa calculará el promedio de los números"
                + "ingresados, hasta que ingrese un número negativo");
        
        do{        
            System.out.println("Escriba un número: ");
     
            numero = Integer.parseInt(entrada.nextLine());
            suma += numero;        
            contador ++;
            
        }while(numero >= 0);
        suma -=numero; //Esto es lo que se me ocurrió pata que funcione
        contador --;
  
        System.out.println("El promedio de los números ingresados es " +suma/contador);
    
    }
}
    

