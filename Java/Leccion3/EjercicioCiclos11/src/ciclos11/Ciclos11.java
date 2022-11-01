
import javax.swing.JOptionPane;

/*
Ejercicio 11: Diseñar un programa que muestre el producto de los 10 primeros 
números impares.
Hacerlo con JOptionpane
*/
public class Ciclos11 {//Estoy tratando de memorizar los pasos, así es que voy 
                        // a documentar paso a paso
    //Lo primero es llamar al método main
    public static void main(String[] args) {
        //Como vamos a usar JOptionPane, definimos las variables. En principio
        //se necesitan tres: número, producto y un contador, todos de clase entero
        //El int se coloca una sola vez. Se inicializan las variables:
        int numero = 1, producto = 1, contador = 0;
        //Imprimimos una línea que explicará qué hace el código con una ventana
        JOptionPane.showMessageDialog(null, "El siguiente programa calculará el producto de los "
                + "diez primeros números impares ");
        
        //Hacemos un bucle con do-while para que el código repita la operación hasta
        //que el contador llegue a un valor menor a 10.
        do{
            producto *= numero;
            contador +=1;
            numero +=2;
            
            }while(contador <10);
        
//La ventana de mensaje mostrará el resultado de la operación:        
        JOptionPane.showMessageDialog(null, "el producto de los diez primeros números "
                + "impares es: "+producto);
                }
        }

