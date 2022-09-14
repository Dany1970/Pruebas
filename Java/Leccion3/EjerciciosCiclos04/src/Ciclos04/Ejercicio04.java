/*
Ejercicio 4: Pedir números hasta que se ingrese uno negativo y mostrat cuántos
números se han ingresado. Primero con Clase Scanner
 
package Ciclos04;

import java.util.Scanner;

public class Ejercicio04 {
    public static void main(String[] args) {
        Scanner consola = new Scanner(System.in);
        System.out.println("Escriba un número: ");
        var numero = Integer.parseInt(consola.nextLine());
        
        var contador = 0; //
                            
        while(numero >= 0){
            contador++; //Vamos aumentando el contador en uno
            System.out.println("Escriba otro número: ");
            numero = Integer.parseInt(consola.nextLine());
            }
        System.out.println("Se han ingresado " +contador +" números no negativos");
    }
    
}
*/