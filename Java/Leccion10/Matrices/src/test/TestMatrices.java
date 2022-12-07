
package test;

import domain.Persona;


public class TestMatrices {
    public static void main(String[] args) {
        int edades[][] = new int[3][2]; //filas y columnas
        System.out.println("edades = " + edades);
        //LLenado manual de la matriz
        edades[0][0] = 5;
        edades[0][1] = 7;
        edades[1][0] = 8;
        edades[1][1] = 4;
        edades[2][0] = 3;
        edades[2][1] = 6;
        
        System.out.println("edades 0-0: "+edades[0][0]);
        System.out.println("edades 0-1:"+edades[0][1]);
        System.out.println("edades 1-0: "+edades[1][0]);
        System.out.println("edades 1-1:"+edades[1][1]);
        System.out.println("edades 2-0: "+edades[2][0]);
        System.out.println("edades 2-1:"+edades[2][1]);
        
        //ciclo for anidado dentro de otro para generar la matriz
        System.out.println("Recorremos la matriz a través del ciclo for");
        for (int fila = 0; fila < edades.length; fila++) {
            for (int col = 0; col < edades[fila].length; col++) {
                System.out.println("edades "+fila+"-"+col+" :"+edades[fila][col]);
                
                
            }
           //Sintaxis clásica
           //String frutas[][] = new String[3][2];
           
           //Sintaxis simplificada
           String frutas[][] = {{"Limón","Pomelo"},{"Ciruela","Kiwi"},{"Banana","Manzana"}};
           imprimir(frutas);
           /*
           for (int i = 0; i < frutas.length; i++) {
            for (int j = 0; j < frutas[i].length; j++) {
                System.out.println("frutas "+i+"-"+j+" :"+frutas[i][j]);
           
                   
           }
        }
*/
           //Creamos una matriz de objetos
           Persona personas[][] = new Persona[2][3];
           //Asignamos valores a la matriz manualmente
           personas[0][0] = new Persona("Ariel");
           personas[0][1] = new Persona("Osvaldo");        
           personas[0][2] = new Persona("Natalia");
           personas[1][0] = new Persona("Programación");
           personas[1][1] = new Persona("Estadística");        
           personas[1][2] = new Persona("AySO");
            System.out.println("Matriz de personas: ");
           imprimir(personas);
    }
    }
public static void imprimir(Object matriz[][]){
    for (int i = 0; i < matriz.length; i++) {
        for (int j = 0; j < matriz[i].length; j++) {
            System.out.println("matriz "+i+"-"+j+" :"+matriz[i][j]);
               }
    }
}
}
     


