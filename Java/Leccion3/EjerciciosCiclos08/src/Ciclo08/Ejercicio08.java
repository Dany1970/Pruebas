package Ciclo08;

import javax.swing.JOptionPane;

/*
EjercicioCiclo08: perdir un número n al ususario u mostrar todos los números del 1 al n
*/
public class Ejercicio08 {
    public static void main(String[] args) {
        System.out.println("Digite un número: ");
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número"));
        int i = 1;
        while(i <= numero){
            JOptionPane.showMessageDialog(null, i);
            i++;
    }
}
}