/*
Ejercicio 4: Pedir números hasta que se ingrese uno negativo y mostrat cuántos
números se han ingresado. Con clase JOptionPane
 */
package Ciclos04;

import javax.swing.JOptionPane;

public class Ciclos04 {
    public static void main(String[] args) {
        int numero, contador;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        contador = 0;
        while(numero > 0) {
            contador++;
            
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
        }
        JOptionPane.showMessageDialog(null, "Se han ingresado " +contador+ " números no negativos");
            
        }
        
    }
    

