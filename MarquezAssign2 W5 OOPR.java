package com.mycompany.marquezassign2;
import java.util.Scanner;
public class MarquezAssign2 {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Greatest Value of three numbers:");
        System.out.print("Enter first number: ");
        int x = scanner.nextInt();
        System.out.print("Enter second  number: ");
        int y = scanner.nextInt();
        System.out.print("Enter third  number: ");
        int z = scanner.nextInt();
        
        System.out.println(" ");
  
        if (x>y && x>z){
            System.out.print("The highest number is: "+ x);    
        }
        else if (y>x && y>z){
            System.out.print("The highest number is: "+ y);    
        }
        else if (z>y && z>x){
            System.out.print("The highest number is: "+ z);    
        }
        
        
    }
}
