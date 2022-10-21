/*
/*Ejercicio 06: Pedir números hasta que se teclee un cero. Mostrar la suma de todos los 
números introducidos usando JOptionPane

*/
package Ciclos06;

import javax.swing.JOptionPane;

public class Ejercicio06 {
    public static void main(String[] args) {
        int numero, suma = 0;
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número entero: "));
            suma += numero;
            }while(numero != 0);
    
        JOptionPane.showMessageDialog(null, "La suma de los números ingresados es " +suma );
        
    }
    }
    
