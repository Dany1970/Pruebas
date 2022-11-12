/*
Ejercicio 3: Leer 5 números por teclado, almacenarlos en un arreglo y a continuación
realizar la media de los números positivos, la media de los negativos y contar el 
número de ceros
 */
package arreglos_ejercicio_3;

import javax.swing.JOptionPane;


public class Arreglos_Ejercicio_3 {
    public static void main(String[] args) {
        int contador1, contador2, contador3, suma1, suma2;
        int numeros[] = new int[5];
        contador1 = 0; suma1 = 0; contador2 = 0; contador3 = 0; suma2 = 0;
        for(int i = 0; i < 5; i ++){
            numeros[i] = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
            if(numeros[i] > 0) {
            contador1++;
            suma1 += numeros[i];
                        }
            else if(numeros[i] < 0){
                contador2++;
            suma2 += numeros[i];
                    }
            else{
                contador3++;
            }
        }
    if(suma1 == 0){
        JOptionPane.showMessageDialog(null, "No se puede obtener la media de los números positivos porque "
                        + "no se ha ingresado ningún número positivo");
                              }
    else{            
        JOptionPane.showMessageDialog(null, "El promedio de los números positivos es " +suma1/contador1);
                }
    if(suma2 == 0){
        JOptionPane.showMessageDialog(null, "No se puede obtener la media de los números negativos porque "
                        + "no se ha ingresado ningún número negativo");
                              }
    else{            
        JOptionPane.showMessageDialog(null, "El promedio de los números negativos es " +suma2/contador2);
                    }
    JOptionPane.showMessageDialog(null, "La cantidad de ceros es "+contador3);
                    }
    }

