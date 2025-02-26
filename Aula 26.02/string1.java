public class string1 {
    
    public static void main (String args []){
        String nome = "Pão de Gliter";
        String str = "alunos";

        System.out.println(nome);
        System.out.println(str);
        System.out.println(str + ":" + nome);     
        //**********************************************
        String str2 = new String("Gabriel");
        String str3 = new String("Carvalho");
        System.out.println("Esse é o String 2:" + str2);
        System.out.println( str2 + " " + str3);
        
        System.out.println(str2.concat(str3).toUpperCase() + "."+ "*** Esta é a concatem");
        System.out.println("Quantidade de caractere:" + str2.length());
        System.out.println("Quantidade de caractere:" + str3.length());
    }
}
-