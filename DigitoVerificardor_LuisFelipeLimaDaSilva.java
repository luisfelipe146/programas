/*
CURSO: ANÁLISE E
DESENVOLVIMENTO DE SISTEMAS

Aluno (a): Luis Felipe Lima da Silva
Disciplina: Lógica de Programação
*/
import java.util.Scanner;
class Main{
    public static void main(String[] args) {
      int DV1,DV2,resul,dig1,dig2,dig3,dig4,dig5,dig6,dig7,dig8,dig9,soma1,soma2,teste1,teste2,vlr_final;
      while(true){
        System.out.println("--------------------------------------------\nEscolha as opções:\n[1]-Verificar o dígito verificador do CPF\n[2]-Informações do desenvolvedor\n[3]-Sair do algoritmo\n--------------------------------------------");
        Scanner menu = new Scanner(System.in);
        resul = menu.nextInt();
        if (resul == 1) {
          System.out.printf("___.___.___-??\nInforme o seu CPF com os 9 dígitos separadamente\n>");
          Scanner vlr1 = new Scanner(System.in);
          dig1 = vlr1.nextInt();
          System.out.printf("\n"+dig1+"__.___.___-??\n>");
          Scanner vlr2 = new Scanner(System.in);
          dig2 = vlr2.nextInt();
          System.out.printf("\n"+dig1+dig2+"_.___.___-??\n>");
          Scanner vlr3 = new Scanner(System.in);
          dig3 = vlr3.nextInt();
          System.out.printf("\n"+dig1+dig2+dig3+".___.___-??\n>");
          Scanner vlr4 = new Scanner(System.in);
          dig4 = vlr4.nextInt();
          System.out.printf("\n"+dig1+dig2+dig3+"."+dig4+"__.___-??\n>");
          Scanner vlr5 = new Scanner(System.in);
          dig5 = vlr5.nextInt();
          System.out.printf("\n"+dig1+dig2+dig3+"."+dig4+dig5+"_.___-??\n>");
          Scanner vlr6 = new Scanner(System.in);
          dig6 = vlr6.nextInt();
          System.out.printf("\n"+dig1+dig2+dig3+"."+dig4+dig5+dig6+".___-??\n>");
          Scanner vlr7 = new Scanner(System.in);
          dig7 = vlr7.nextInt();
          System.out.printf("\n"+dig1+dig2+dig3+"."+dig4+dig5+dig6+"."+dig7+"__-??\n>");
          Scanner vlr8 = new Scanner(System.in);
          dig8 = vlr8.nextInt();
          System.out.printf("\n"+dig1+dig2+dig3+"."+dig4+dig5+dig6+"."+dig7+dig8+"_-??\n>");
          Scanner vlr9 = new Scanner(System.in);
          dig9 = vlr9.nextInt();
          System.out.printf("\n"+dig1+dig2+dig3+"."+dig4+dig5+dig6+"."+dig7+dig8+dig9+"-??\n>");
          soma1=(2*dig9)+(3*dig8)+(4*dig7)+(5*dig6)+(6*dig5)+(7*dig4)+(8*dig3)+(9*dig2)+(10*dig1);
          soma2=(3*dig9)+(4*dig8)+(5*dig7)+(6*dig6)+(7*dig5)+(8*dig4)+(9*dig3)+(10*dig2)+(11*dig1);
          DV1=(soma1*10)%11;
          if (DV1 == 10){
            DV1=0;
          }
          DV2=((soma2+DV1*2)*10)%11;
          if (DV2 == 10){
            DV2=0;
          }
          vlr_final=DV1*10+DV2;
          System.out.println("\n\nÚltimos digitos que faltam:"+vlr_final);
          System.out.println("\n\n\nSeu CPF Completo:\n\t"+dig1+dig2+dig3+"."+dig4+dig5+dig6+"."+dig7+dig8+dig9+"-"+vlr_final+"\n\n");
        }
        else if (resul == 2) {
          System.out.println("\n\tluisfelipe146@hotmail.com\nLuis Felipe Lima da Silva\n\n");
        }
        else if (resul == 3) {
          System.out.printf("Saindo...\n");
          break;
        }
        else{
          System.out.printf("Digite uma opção válida!\n\n");
        }
      }
  }
}
