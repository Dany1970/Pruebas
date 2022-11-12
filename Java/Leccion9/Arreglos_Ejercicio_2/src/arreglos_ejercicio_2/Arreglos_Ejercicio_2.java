/*
Ejercicio 2: Leer 5 números, guardarlos en un arreglo y mostrarlos 
en el orden inverso al introducido.
*/

package arreglos_ejercicio_2;

import java.util.Scanner;

public class Arreglos_Ejercicio_2 {
    public static void main(String[] args) {
       Scanner consola = new Scanner(System.in);
       int numeros[] = new int[5];
       
       for(int i = 0; i < 5; i ++){
            System.out.println("Digite un número :");
            numeros[i] = Integer.parseInt(consola.nextLine());               
        }
        for(int i = 4; i >= 0; i --){
            System.out.println("El "+(i+1)+"° número ingresado es "+numeros[i]);
    }
}
}
