package Ciclos09;

import java.util.Scanner;

/*
EjercicioCiclos09:
Pedir el día, mes y año de una fecha e indicar si la fecha es correcta
Suponiendo que todos los meses son de 30 días.
Cuando tenga tiempo, lo voy a modificar para distintos meses, y otra cosa que me pareció, comprobar antes de seguir
ejecutando el código , el error, para ahorrar tiempo de ejecución. 
*/

public class Ciclos09 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
                System.out.println("Ingrese el día: ");
                int dia = Integer.parseInt(entrada.nextLine());
                System.out.println("Ingrese el mes: ");
                int mes = Integer.parseInt(entrada.nextLine());
                System.out.println("Ingrese el año: ");
                int anio = Integer.parseInt(entrada.nextLine());
                
                if((dia != 0) && (dia <= 30)){
                    if((mes != 0) && (mes <= 12)){
                        if((anio !=0) && (anio <= 2022)){
                            System.out.println("La fecha ingresada es: "+dia+"/"+mes+"/"+anio);
                        }
                        else{
                            System.out.println("Fecha incorrecta, año incorrecto");
                        }
                        
                                }
                        else{
                                System.out.println("Fecha incorrecta, mes incorrecto");
                    }
                }
                else{
                    System.out.println("Fecha incorrecta, día incorrecto" );
                }
                
                
    }
 
}
