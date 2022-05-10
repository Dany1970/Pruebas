import java.util.Scanner;

public class HolaMundo {
    public static void main(String[] args) {
        /*System.out.println("Hola Mundo desde Java");//println es salto de línea
        
        int miVariable = 10; //definiendo una variable primitiva de tipo entera
                        // no olvidar el punto y coma como en PSEint, no así en Python
        System.out.println(miVariable);
        miVariable = 5; //reutilizamos la variable, no hace falta definirla porque ya está definida
        System.out.println(miVariable);
        //Acá habló sobre alcance de una variable: si está definids dentro de un método, no se puede 
        //usar fuera de él
        
        //Tipo string (no es un tipo promitivo, es una clase; comienza con mayúscula)
        
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en programación"; //reutilizando la variable
        System.out.println(miVariableCadena);//Ctrol + click izquierdo muestra dónde
                                            //fue instanciada la variable
        
        
        // Inferencia de tipos - el uso de la palabra reservada var en Java
        //el valor de una variable se conoce como una literal
        // y el tipo de valor, si es tipo int, este será asignado tanto a la variable como a la literal.
        //Una literal de tipo cadena automáticamente será tipo str 
        //a partor de la ver 10 de java podemos utilizar la palabra reservada var en lugar de utilizar el tipo
        //de dato definifo. Podemos utilizar la palabra reservada var para que Java infiera el tipo de dato
        
        var miVariableEntera2 = 10;
        // Hemos creado una variable y le hemos asignado el valor 10; Java infiere el tipo 
        //entero pot el tipo de datos que le asignamos a la derecha. Si le ponemos un caracter,
        //infiere que es char. El uso de var simplifica la asignación de variables
        
        var miVariableCadena2 = "Seguimos estudiando";
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        System.out.println("miVariableCadena2 = " + miVariableCadena2); //Concatenando
        //soutv + Tab
        //Para ejecutar Shift + F6
        
        //Reglas para definir una variable en Java
        /* 
        1- El primer carcater puede ser culauier letra en maypuscula o minúscula, 
        pero se recomienda por conveción camelCase
        2- No se pueden usar números al comienzo del nombre
        3- No puede tener caracteres especiales
        4- No usar acentos en los nombres de las variables (aunque el programa lo permite)
        5- Se puede usar guión bajo
        6- No se puede comenzar con numeral (es ilegal)
        7- No puede ser una variable reservada (ver archivo)
        
        
        
        //Ejercicio de concatenación
      
        var nombre = "Jorge";
        var apellido = "Lista";
        var union = nombre +" " + apellido;
        System.out.println("union = " + union);
        
        
        var a = 8;
        var b = 7;
        System.out.println(a + b);
        //var identifica que la variable es entera, así es que el operador de suma
        //simplemente suma, no concatena
        /*El código compila de izquierda a derecha, esto significa que si tenemos una cadena
        primero y luego números, los concatena todos como cadenas. Si se desea 
        concatenar y sumar, se deben colocar los números entre paréntesis.
        Ejemplo: 
        
        System.out.println(nombre + a + b);
        System.out.println(nombre + (a + b));
        
        // Caracteres especiales con Java
        
        var nombre1 = "Victoria"; //Código duro, nosotros le estamos asignando valor a las variables
        System.out.println(nombre1); //Esto es lo que veníamos haciendo
        // Vamos a usar un conjunto de caracteres para introducir una línea en una concatenación
        System.out.println("Nueva Línea: \n" + nombre1);//NOTA IMPORTANTE: los caracteres
        //especiales se colocan dentro de las comillas
        //Para colocar un salto de línea entre las salidas de impresión:
        System.out.println("\nNueva Línea: \n" + nombre1);
        
        System.out.println("Tabulador: \t" + nombre1);//coloca un espacio de tabulación
        
        //*iMPRTANTE*: CON format te deja todo prolijito
        
        //Un espacio para volver: caracter de retroceso
        System.out.println("Retroceso: \b" + nombre);//borra un caracter hacia atrás
        System.out.println("Retroceso:\b" + nombre);
        
        //Comillas
        System.out.println("Comillas simples: \'" + nombre + "\'");
        System.out.println("Comillas dobles: \"" + nombre + "\"");
       
        //Clase Scanner
        //Sintaxis para crear un objeto de la clase entrada, llamada entrada
        //Se importa porque se encuentra definida en otro paquete llamado Java.
        //Cuando lo creamos, se "carga" el paquete en forma automática, y si no
        //hay que hacerlo manual. Aparece arriba de todo al inicio del código:
        // import java.util.Scanner; Ahí ya está habilitado
        
        Scanner entrada = new Scanner(System.in); //Activamos un objeto de la
        //clase scanner, que odentificamos como "entrada". Podría ser también "consola"
        // ya que identificará las entradas de usuario por consola:
        
        System.out.println("Escriba su nombre: ");
        var nombre2 = entrada.nextLine();//Se ingresará una variable de tipo str
        //nextLine es para leer una línea completa de la consola y detiene la ejecución
        //del programa para que el usuario ingrese datos
        System.out.println("Escriba su profesión");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: " +titulo2 +" " +nombre2);
        */
        /*
        //Tipos primitivos
        byte numeroEnteroByte = 10; //Una literal de tipo entero primitivo byte.
        System.out.println("Numero entero byte: "+ numeroEnteroByte);
        //Cada tipo de dato tiene un rango, debemos sabe el valor min y max que 
        //puede almacenar el tipo byte
        System.out.println("Valor mínimo del byte: "+ Byte.MIN_VALUE); 
        System.out.println("Valor máximo del byte: "+ Byte.MAX_VALUE);
        //El valor mínimo del tipo byte es -128 y el máx 127 (puede ser negativo)
           
         short numeroEnteroShort = -32000; //Una literal de tipo entero primitivo short. 
         System.out.println("Numero entero short: "+ numeroEnteroShort);
        //Cada tipo de dato tiene un rango, debemos sabe el valor min y max que 
        //puede almacenar el tipo byte
        System.out.println("Valor mínimo del byte: "+ Short.MIN_VALUE); 
        System.out.println("Valor máximo del byte: "+ Short.MAX_VALUE);
        //El valor mínimo del tipo byte es -128 y el máx 127 (puede ser negativo)
        
        //La forma de evaluar los valores mínimo y máximo es usando su clase Short o Byte
        //(nota importante: las clases van en Mayúscula)
        
        //Debido a estas limitaciones de los tipos byte y short, se recomienda usar el 
        //tipo primitivo int 
        
        int numeroEnteroint = 320000; 
        System.out.println("Numero entero int: "+ numeroEnteroint);
        System.out.println("Valor mínimo del byte: "+ Integer.MIN_VALUE); 
        System.out.println("Valor máximo del byte: "+ Integer.MAX_VALUE);
        
        //Tipo entero primitivo long
        
       long numeroEnterolong = 320000000; 
       System.out.println("Numero entero long: "+ numeroEnterolong);
       System.out.println("Valor mínimo del byte: "+ Long.MIN_VALUE); 
       System.out.println("Valor máximo del byte: "+ Long.MAX_VALUE);
*/
       
        //Tipo primitivo float
        
        //float numFloat = 10.0F; //Notar el uso de la F (o f) para que no de error
        
        //Clase 5:Inferencia de tipos var y tipos primitivos
        /*
        var numEntero = 20;//las literales in punto son automáticamente de tipo entero
        System.out.println("numEntero = " +numEntero);
        
        var numFloat = 10.0F;//Automáticamente con el punto decimal se tanforma en tipo double
        System.out.println("numFloat = " + numFloat);
        
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);
      */  
    //Para hacer el paso a paso (step over, marcar el punto de quiebre, seleccionar 
    //debug file y darle F8) 
    //Para que se tome al dato como float, hay que agregar la F (mirar 10.0F)
    
        char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);
        
        char varCaracter = '\u0024';//estamos poniendo el caracter $ con el código unicode
        System.out.println("varCaracter = " + varCaracter);
       
        char varCaracterDecimal = 36;//estamos poniendo el caracter con valor decimal 
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        
        char varCaracterTeclado = '$';//estamos poniendo el caracter $ con el teclado 
        System.out.println("varCaracterTeclado = " + varCaracterTeclado);
        
        //Los códigos unicode son útiles para caracteres que no tenemos en el teclado
        
        var varCaracter1 = '\u0024';//estamos poniendo el caracter $ con el código unicode
        System.out.println("varCaracter1 = " + varCaracter1);
       
        var varCaracterDecimal1 = 36;//estamos poniendo el caracter con valor decimal 
        System.out.println("varCaracterDecimal1 = " + varCaracterDecimal1);
        
        var varCaracterTeclado1 = '$';//estamos poniendo el caracter $ con el teclado 
        System.out.println("varCaracterTeclado1 = " + varCaracterTeclado1);
        
        //con var, va a hacer una inferencia de tipos, así es que en este caso al valor 
        //numérico, no lo va a tomar como un valor de código unicode, si no que lo va a tomar 
        //como un tipo entero 
       
        int varEnteroChar = '$';
        System.out.println("varEnteroChar = " + varEnteroChar);
        
        int caracter = 'b';
        System.out.println("caracter= " + caracter);
        
        // En el primer caso, al colocar int, "convierte" el código unicode a número, según
        //le corresponde en la tabla
        //En el segundo caso, igual
        
        
} 
    }   
    

              