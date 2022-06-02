package Ejercicio4;

import java.util.Scanner;

public class Ejercicio4 {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);//para que se importe Scanner, hacer clcik sobre el foco y darle a import
        System.out.println("Digite un número = ");
        int num1;
        num1 = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite otro número");
        int num2 = Integer.parseInt(entrada.nextLine());
        System.out.println("El número mayor es: ");
        System.out.println(num1 > num2 ? num1 : num2);
        
        

    }

}
