
package CicloWhile;

public class EjercicioWhile01 {
// Vamos a comenzar con los ciclos. los ciclos tienen que ver con la repetición de códigos.
// Se revisa la condición, mientras sea verdadera, se repite el código, hasta que sea falso
// Vamos a ver el ciclo While
// Creamos la clase mail con el psvm
public static void main(String[] args) {
var conteo = 0; //Inferencia de tipos
while (conteo < 3) {
System.out.println("conteo = " + conteo);
conteo ++; // Vamos aumentando en uno la variable
}

//En el ciclo do - while, primero se ejecuta el código 
// y luego se verifica la condición

var contador = 0;
do{
    System.out.println("contador = " + contador);
    contador ++;
}while(contador < 7);
}
{
    
}