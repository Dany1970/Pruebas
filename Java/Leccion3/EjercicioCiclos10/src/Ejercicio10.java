import javax.swing.JOptionPane;

public class Ejercicio10 {
    public static void main(String[] args) {
        int numero, suma = 0, contador = 0;
         System.out.println("El siguiente programa calculará la suma de diez números "
                + "ingresados");
               
        do{        
            numero = Integer.parseInt(JOPtionPane.showInputDialog("Ingrese un número: "));
            suma += numero;        
            contador ++;
            
        }while(contador < 10);
        System.out.println("La suma de los números ingresados es; "+suma);
}
    
}
