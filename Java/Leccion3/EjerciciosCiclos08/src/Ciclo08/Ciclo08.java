package Ciclo08;

import java.util.Scanner;

/*
EjercicioCiclo08: perdir un número n al ususario u mostrar todos los números del 1 al n
*/

public class Ciclo08 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un número: ");
        int numero = Integer.parseInt(entrada.nextLine());
        int i = 1;
        while(i <= numero){
            System.out.println(i);
            i++;
    }}
}
