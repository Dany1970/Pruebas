
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

//Ciclo for: cuando la condición se cumple, se comienza 
//un incremento o decremento hasta que la condición sea falsa

for(var contando = 0; contando < 7 ; contando++){ //otra forma for(int i = 0...)
// inicializamos el contador y luego va la condición y el incremento
//separados por punto y coma
//se pueden recorrer arreglos, por ejemplo con un for
    System.out.println("contando = " + contando);
} 
}
}