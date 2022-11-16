/*
Ejercicio 12: Pedir un número y calcular su factorial. Hacerlo con las dos clases, 
Scanner y JOptionPane (en una misma plantilla)
*/
package Ciclos12;

//import java.util.Scanner;
import javax.swing.JOptionPane;


public class Ciclos12 {
    public static void main(String[] args) {
        //Primero usamos la clase scanner
        //Scanner entrada = new Scanner(System.in);
        long factorial = 1; //el factorial puede ser un número muy grande)
        //System.out.println("Digite un número ");
        //var numero = Integer.parseInt(entrada.nextLine());
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        for(int i = 1; i<=numero; i ++){
            factorial *= i;
         }
        //System.out.println("El factorial del númrro ingresado es: " +factorial);
        JOptionPane.showMessageDialog(null, "El factorial del número ingresado es: "+factorial);
    }
}
