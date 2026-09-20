package com.mycompany.marquezact1;
import java.util.Scanner;
public class MarquezAct1 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String choice;
    do {
        System.out.println ("Input Your GRADES\n");
       
       System.out.println ("Java: ");
       float jav = scanner.nextFloat();
       
       System.out.println ("C : ");
       float cg = scanner.nextFloat();
       
       System.out.println ("Database Handling : ");
       float db = scanner.nextFloat();
       double ave = (cg+jav+db)/3;
    if(ave < 75){
       System.out.println ("The average grade of the student is: "+ave+" so the student's grade is F");
       }
    else if(ave < 79){
       System.out.println ("The average grade of the student is: "+ave+", so the student's grade is C");
       }
    else if(ave < 89){
       System.out.println ("The average grade of the student is: "+ave+", so the student's grade is B");
       }
    else if(ave < 100){
       System.out.println ("The average grade of the student is: "+ave+", so the student's grade is A");
       }
    System.out.println ("Do you want to continue? (Yes/No) : ");
    choice = scanner.next();
    }
    
    
    while (choice.equalsIgnoreCase("YES"));
    }
  
   
}
