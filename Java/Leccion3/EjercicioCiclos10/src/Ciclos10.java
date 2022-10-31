
import java.util.Scanner;

/*Ejercicio 10: Pedir 10 números y escribir la suma total. Con clase scanner y 
JOptionPane

*/
public class Ciclos10 {
    public static void main(String[] args) {
        int numero, suma = 0, contador = 0;
        Scanner consola =new Scanner(System.in);
        System.out.println("El siguiente programa calculará la suma de diez números "
                + "ingresados");
        do{        
            System.out.println("Ingrese un número: ");
            numero = Integer.parseInt(consola.nextLine());
            suma += numero;        
            contador ++;
            
        }while(contador < 10);
        System.out.println("La suma de los números ingresados es; "+suma);
        }  
    
      
        
        }
    

