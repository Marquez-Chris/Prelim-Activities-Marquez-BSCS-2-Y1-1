package com.mycompany.marquezassign1w5;
import java.util.Scanner;
public class MarquezAssign1W5 {

    public static void main(String[] args) {
        System.out.println("Hello World!");
        
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter First word: ");
        String usrinput = scanner.nextLine();
        System.out.print("Enter Second word: ");
        String usrinput2 = scanner.nextLine();
        System.out.print("Enter Third word: ");
        String usrinput3 = scanner.nextLine();
        System.out.print(usrinput + " " + usrinput2 + " " + usrinput3 + " ");
    }
}
