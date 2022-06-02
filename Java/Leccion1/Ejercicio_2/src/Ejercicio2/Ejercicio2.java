

        
package Ejercicio2;

import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
        //Hacer un programa que calcule e imprima el salario de un empleado
        //a partir de sus horas semanales trabajadas y de su salario por hora.

    Scanner entrada = new Scanner(System.in);
        
        int horas;
        float salario, salariosemanal;
        
        System.out.println("Escriba las horas que trabaja por semana");
        horas = Integer.parseInt(entrada.nextLine());
        System.out.println("Escriba su salario por hora: ");
        salario = Float.parseFloat(entrada.nextLine());
         
        salariosemanal = salario * horas;
        System.out.println("\nEl salario semanal: U$s" +salariosemanal);      
    }
}
