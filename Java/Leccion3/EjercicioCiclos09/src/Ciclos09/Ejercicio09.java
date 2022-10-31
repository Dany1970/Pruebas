 package Ciclos09;

import javax.swing.JOptionPane;


public class Ejercicio09 {
    /*
EjercicioCiclos09:
Pedir el día, mes y año de una fecha e indicar si la fecha es correcta
Suponiendo que todos los meses son de 30 días.
Cuando tenga tiempo, lo voy a modificar para distintos meses, y otra cosa que me 
pareció, comprobar antes de seguir
ejecutando el código , el error, para ahorrar tiempo de ejecución. 
*/
    public static void main(String[] args) {
        System.out.println("Ingrese el día: ");
        int dia = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el día"));
        System.out.println("Ingrese el mes: ");
        int mes = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el mes"));
        System.out.println("Ingrese el año: ");
        int anio = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el año"));
            if((dia != 0) && (dia <= 30)){
                    if((mes != 0) && (mes <= 12)){
                        if((anio !=0) && (anio <= 2022)){
                            JOptionPane.showMessageDialog(null, "La fecha ingresada es: "
                                    + ""+dia+"/"+mes+"/"+anio);
                        }
                        else{
                            JOptionPane.showMessageDialog(null, "Fecha incorrecta, "
                                    + "año incorrecto");
                        }
                        
                                }
                        else{
                                JOptionPane.showMessageDialog(null, "Fecha "
                                        + "incorrecta, mes incorrecto");
                    }
                }
                else{
                    JOptionPane.showMessageDialog(null, "Fecha incorrecta, día "
                            + "incorrecto" );
                }
              
              
    }
 
}

    
