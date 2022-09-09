package CicloWhile;


public class EjercicioWhile01 {
//Vamos a ver cómo funcionan los diferentes ciclos, que se ejecutan mientras una condición sea verdadera
    //, y algunas palabras que pueden usarse para parar o continuar el mismo

//Ciclo While
public static void main(String[] args) {
        var conteo = 0; //Inferencia de tipos
        while(conteo < 7){
            System.out.println("conteo = " + conteo);
            conteo++; //Vamos aumentando el contador en uno
        }
//Ciclo do while
        var contador = 0;
        do{
        System.out.println("contador = " + contador);
        contador++;
        }while(contador < 7);

//Ciclo for
inicio:
        for(var contando = 0; contando < 7; contando++){ 
        //también se pude poner int i = 0
            if(contando % 2 == 0){
                System.out.println("contando = " + contando);
                break inicio;
}
        for(var contando1 = 0; contando1 < 7; contando1++){ 
            if(contando1 % 2 != 0){
                continue;
            }
                System.out.println("contando1 = " + contando1);
                   
}
        //Etiquetas (Labels)
        //Se combinan con la palabras break y continue 
        // para ir a un lugar específico de nuestro programa
        // no es muy recomendable, pero es bueno conocerlo (programación
        //de tipo GOTO) Tienen mayor uso en ciclos anidados
        // Ver el código arriba (no se notan los cambios en estos casos)
}
}
}
    
    

