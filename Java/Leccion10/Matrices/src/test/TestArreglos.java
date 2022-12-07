
package test;
// los arreglos se ponene entre corchetes, pueden ir pegados o no al identificador
//o adelante del identificador. Lo que más se usa es pegado
public class TestArreglos {
    public static void main(String[] args) {
        int edades[] = new int[3];//generaremos un arreglo con tipos enteros
            // los arreglos son de tipo object, se heredan de la clase objest por eso va new
            // en el lado izquierdo estamos declarando la variable, en el lado derecho, instanciamos 
            //un ibjeto de tipo object
            //la cantidades asignada de elementos no se puede cambiar
            System.out.println("edades = " + edades);
            
            edades[0] = 17;//los índice empiezan en 0
            System.out.println("edades 0= " + edades[0]);
            //Modificar el índice 1 y 2, y mostrar cada uno
            edades[1] = 52;
            System.out.println("edades 1 = " + edades[1]);
            edades[2] = 68;
            System.out.println("edades 2 = " + edades[2]);
            
            //edades[3] = 7;//ERROR: array index out of band exception; error en tiempo 
            //de ejecución, es decir, el compilador compila, pero muestra el error
            
            for(int i = 0; i < edades.length; i ++){
                System.out.println("edades y sus elementos "+i+": "+edades[i]);
            }
    }
 
}
 