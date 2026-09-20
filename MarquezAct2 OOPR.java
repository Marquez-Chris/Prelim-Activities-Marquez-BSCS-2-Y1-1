package com.mycompany.marquezact2;
import java.util.Scanner;
public class MarquezAct2 {

    public static void main(String[] args) {
        String choice;
        Scanner scanner = new Scanner(System.in);
        
       do{
           System.out.println("Variable Values:");
       
        System.out.print("X = ");
        float x = scanner.nextFloat();
        System.out.print("y = ");
        float y = scanner.nextFloat();
        
        System.out.println(" ");
        System.out.println(" ");
        System.out.println(" ");
        System.out.println("Arithmetic Operation: ");
        double add = x + y; 
        System.out.println("Addition: x + y = " + add);
        double sub = x - y; 
        System.out.println("Subtraction: x - y = " + sub);
        double mul = x * y; 
        System.out.println("Multiplication: x - y = " + mul);
        double dib = x / y; 
        System.out.println("Division: x - y = " + dib);
        double mod = x % y; 
        System.out.println("Modulus: x % y = " + mod);
        double inc = ++x; 
        System.out.println("Increment x++ = " + inc);
        double dec = --x; 
        System.out.println("Decrement x-- = " + dec);
        
        System.out.println ("Do you want to continue? (Yes/No) : ");
        choice = scanner.next();
        
       }
       while (choice.equalsIgnoreCase("YES"));
        
        
        
        
    }
}
