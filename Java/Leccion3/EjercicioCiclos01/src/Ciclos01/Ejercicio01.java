//Ejercicio 1: Leer un númmero y mostrar su cuadrado, repetir 
// el proceso hasta que se introduzca un número negativo
//Vamos a ver un método de entrada y salida pero con la clase JOptionPane
package Ciclos01;

import javax.swing.JOptionPane;

public class Ejercicio01 {
    public static void main(String[] args) {
              
        int numero, cuadrado; //Definimos las variables a usar
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: ")); 
        while(numero >= 0) { //Acá se inicia el ciclo
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El número" +numero+ "elevado al cuadrado es: " +cuadrado);
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
            
        }
        System.out.println("El programa ha finalizado por ingresar un número negativo");
                
    }
    }
    

