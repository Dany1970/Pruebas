
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
        //a partir de la ver 10 de java podemos utilizar la palabra reservada var en lugar de utilizar el tipo
        //de dato definido. Podemos utilizar la palabra reservada var para que Java infiera el tipo de dato
        
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
        1- El primer carcater puede ser cualquier letra en mayúscula o minúscula, 
        pero se recomienda por convención camelCase
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
        
         //Activamos un objeto de la
        //claseScanner entrada = new Scanner(System.in); scanner, que odentificamos como "entrada". Podría ser también "consola"
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
        var numEntero = 20;//las literales sin punto son automáticamente de tipo entero
        System.out.println("numEntero = " +numEntero);
        
        var numFloat = 10.0F;//Automáticamente con el punto decimal se tranforma en tipo double
        System.out.println("numFloat = " + numFloat);
        
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);
         */
        //Para hacer el paso a paso (step over, marcar el punto de quiebre, seleccionar 
        //debug file y darle F8) 
        //Para que se tome al dato como float, hay que agregar la F (mirar 10.0F)
        /*
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
        
         */
        //Tipos primitivos booleanos
        // Sólo tienen dos valores True False
        //creamos una variable:
        /*
    var varBool = false; //Nótese la letra f (o t) minúscula
    System.out.println("varBool = " + varBool);
    
    if (varBool){ // Cuando una var es booleana no hace falta poner a qué es igual
            System.out.println("La bandera es verde"); 
    }// Ojo acá van llaves
    else{
        System.out.println("La bandera es roja");
    }
    //chequear cambiando la variable dura false por true
    //Algoritmo ¿Es mayor de edad?
    var edad = 15; //literal tener presente la inferencia de tipos
    var adulto = edad >= 18; //Esta es una expresión booleana
    if(adulto) {
        System.out.println("Eres mayor de edad");
    }
    else{
        System.out.println("Eres menor de edad");
    }

  //Cambiar la edad para verificar el programa
  //Otra forma:
  var edad1 = 19; //literal tener presente la inferencia de tipos
    if(edad1 >= 18) {
        System.out.println("Eres mayor de edad");
    }
    else{
        System.out.println("Eres menor de edad");
  }
         */
        //Conversión de tipoa primitivos
//    var edad = Integer.parseInt("10"); //Convierte un dato de tipo string a un tipo entero
//    //Más adelante vamos a ver cómo crearr nuestro propios métodos. Acá
//    //estamos usando un metodo que ya existe dentro de la clase Integer
//        System.out.println("edad = " + (edad + 1));//Al concatenar, suma porque son enteros
//        
//        //Si no ponemos el método, concatena:
//        var edad1 = "10"; //var tipo string
//    //Más adelante vamos a ver cómo crearr nuestro propios métodos. Acá
//    //estamos usando un metodo que ya existe dentro de la clase Integer
//        System.out.println("edad1 = " + (edad1 + 1)); //Concatena los string
//    var valor01 = Double.parseDouble("3.1416");
//        System.out.println("valor01 = " + valor01);
//        
//    //Ahora vamos a convertir un scanner a tipo entero
//    //Pedir un valor:
//    var entrada = new Scanner(System.in);
//        System.out.println("Digite su edad: ");
//        edad = Integer.parseInt(entrada.nextLine());
//        System.out.println("edad = " + edad);*/
//        
        //Conversión de tipos primitivos en java parte 2
//        var edadTexto = String.valueOf(10);
//        System.out.println("edadTexto = " + edadTexto);
//
//        //falta ver más cosas de la clase 6
//        int num1 = 5, num2 = 4;
//        var solucion = num1 + num2;
//        System.out.println("solucion de la suma = " + solucion);
//
//        solucion = num1 - num2;
//        System.out.println("solucion de la resta = " + solucion);
//
//        solucion = num1 * num2;
//        System.out.println("solucion de la multiplicación = " + solucion);
//
//        solucion = num1 / num2;//sólo la parte entera porque son var de tipo int
//        System.out.println("solucion de la división = " + solucion);
//
//        var solucion2 = 3.4 / num2;//acá ya maneja tipo double al incorporarle el valor tipo double
//        System.out.println("Resultado de la división = " + solucion2);
//
//        solucion = num1 % num2;//Guarda el residuo entero de la divisón
//        System.out.println("solucion = " + solucion);
//
//        if (num1 % 2 == 0) {
//            System.out.println("Es un número par");
//        } else {
//            System.out.println("Es un número impar");//probar con num2
        //En este caso las llaves no son necesarias, pero no entendí bien por qué? 
        //supuestamente después lo veremos
        /*        
        int varNum1 = 5, varNum2 = 4;
        int varNum3 = varNum1 - 6 + varNum2;
            System.out.println("varNum3 = " + varNum3);
        
        varNum1 += 1;
           System.out.println("varNum1 = " + varNum1);
         
        varNum1 -= 1;
        System.out.println("varNum1 = " + varNum1);
        
        varNum1 *= 1;
        System.out.println("varNum1 = " + varNum1);
        
        varNum1 /= 1;
        System.out.println("varNum1 = " + varNum1);
        
        varNum1 %= 2;
        System.out.println("varNum1 = " + varNum1);
         */
       //CLASE 7: 27/MAYO
        //Operadores unarios: Cambio de signo
       /*
        var varA = 7;
        var varB = -varA;
        System.out.println("varA= " + varA);
        System.out.println("varB= " + varB);

        //Operador de negación (aplica para variables de tipo booleanos)
        var varC = true;
        var varD = !varC; //(estamos negando al valor de  la var original)
        System.out.println("varC= " + varC);
        System.out.println("varD= " + varD);

        //Operador unitario de incremento: preincremento
        var varE = 9;
        var varF = ++varE;
        System.out.println("varE = " + varE);//Notar que se incrementa también E
        System.out.println("varF = " + varF);
        //Postincremento: 
        var varG = 3;
        var varH = varG++;
        System.out.println("varG = " + varG);//La g se incrementa en uno
        System.out.println("varH = " + varH);//en H se guarda la G, qué loco

        //Decremento:
        var varI = 4;
        var varJ = --varI;
        System.out.println("varI = " + varI);
        System.out.println("varJ = " + varJ);

        //Postdecremento: 
        var varK = 8;
        var varL = varK--;
        System.out.println("varK = " + varK);
        System.out.println("varL = " + varL);//L guarda el primer valor

        //Operadores de igualdad (==)y relacionales
        var aNum = 5;
        var bNum = 4;//así da False. Si cambiamos por un 5, da True
        var cNum = (aNum == bNum);//Se puede usar paréntesis o no
        System.out.println("cNum = " + cNum);

        var dNum = aNum != bNum;//acá está sin paréntesis e igual funciona
        System.out.println("dNum = " + dNum);

        //Para comparar dos cadenas se usa el método .equals, no el ==
        //Veamos la diferencia:
        
        var cadenaA = "Hello";
        var cadenaB = "Bye bye";
        var cVar = cadenaA == cadenaB;//Compara referencias, no contenidos
        System.out.println("cVar = " + cVar);
        
        var fVar = cadenaA.equals(cadenaB);//Para comparar contenido de objetos de tipo string
        System.out.println("fVar = " + fVar);
        
        //Operadores relacionales
        
        var eNum = (aNum > bNum);//Se puede usar paréntesis o no
        System.out.println("eNum = " + eNum);
        
        var fNum = (aNum >= bNum);//Se puede usar paréntesis o no
        System.out.println("fNum = " + fNum);
        
        //Y así siguiendo se puede usar con < y <= también !=
        
        //También podemos usarlo con una estructura if:
        
        if (aNum % 2 == 0) {
            System.out.println("El número es Par");
        } else {
            System.out.println("El número es impar");
        }
     */   
   // Practicar el algoritmo de mayor de edad con los operadores relacionales
      //oPERADORES CONDICIONALES and (&&) y or (||)
    /*  
      var valorA = 7;
      var valorMinimo = 0;
      var valorMaximo = 10;
      var respuesta = valorA >=valorMinimo && valorA <= valorMaximo;
      
      if (respuesta)
            System.out.println("Está dentro del rango establecido");
      else
            System.out.println("Está fuera del rango establecido");
    
    var vacaciones = true;//Las variables están asignadas con código duro, cambiar para chequear el código
    var dialibre = true;
    
    if (vacaciones || dialibre)
            System.out.println("Papá puede asistir al juego de su hijo");
    else 
            System.out.println("Papá no puede asistir al juego de su hijo");
    
    //OPERADORES TERNARIOS: se usan para simplificar las estructuras if else
    //se recomienda con estructuras sencillas. Si la estructura es más compleja,
    //mejor usar el if - else
   
    var resultadoT = (5 > 8) ? "Verdadero": "Falso" ;
        System.out.println("resultadoT = " + resultadoT);
    
    var numeroT = 7;
    resultadoT = (numeroT % 2 == 0) ? "Par" : "Impar";
        System.out.println("El número es " + resultadoT);        
     */

     //Prioridad de los operadores
/*
    var x = 5;
    var y = 10;
    var z = ++x + y--;
        System.out.println("x = " + x);
        System.out.println("y = " + y);
        System.out.println("z = " + z);
    
    var solucionAritmetica = 4 + 5 * 6 / 3;
        System.out.println("solucionAritmetica = " + solucionAritmetica);
*/
//Ejercicio: área del rectángulo
//Se solicita calcular el área y el perímetro de un rectángulo para esto deberemos 
//crear las variables alto y ancho ambas de tipo int. El usuario debe proporcionar
//los valores de alto, ancho y luego imprimir el resultado, en el sgte formato
//(recuerden no usar acentos, respetar los espacios, mayúsculas, minúsculas y los 
//saltos de línea): Digite el alto del rectángulo. Digite el ancho del rectángulo
//. 
  //Activamos un objeto de la
        claseScanner  = new Scanner(System.in); 
        
        
        System.out.println("Escriba su nombre: ");
        var nombre2 = entrada.nextLine();//Se ingresará una variable de tipo str
        //nextLine es para leer una línea completa de la consola y detiene la ejecución
        //del programa para que el usuario ingrese datos
        System.out.println("Escriba su profesión");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: " +titulo2 +" " +nombre2);
         */
    
    }

}
