/*
Hacemos el mismo ejercicio: Leer un número e indicar si es positivo o negativo. El proceso se repetirá hasta que
se introduzca un cero, per usando la clase JOptionPane
 */
package Ciclos02;

import javax.swing.JOptionPane;

public class Ciclo02 {
    public static void main(String[] args) {
        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while(numero != 0) {
            if(numero > 0) {
                System.out.println("El número " +numero+ " es positivo");
            }
            else{
                System.out.println("El número " +numero+ " es negativo");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
            
        }
        System.out.println("El número " +numero+ " finaliza el programa");
    }
    
}
