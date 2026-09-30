package com.mycompany.marquezmidtermact1;
import java.util.Scanner;


public class MarquezMidtermProj3 {
    public static void main(String[] args) {
        Scanner user = new Scanner(System.in);
        
        int n = 5;
        int[] arr = new int[n];
        
        System.out.print("Enter Data in Array: ");
        for (int i = 0; i < n; i++) {
            arr[i] = user.nextInt();
        }
        
        System.out.print("Stored Data in Array: ");
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
        
        System.out.print("Enter position of Element to Delete: ");
        int pos = user.nextInt();
        
        if (pos < 0 || pos >= n) {
            System.out.println("Invalid position!");
        } else {
            for (int i = pos; i < n - 1; i++) {
                arr[i] = arr[i + 1];
            }
            n--; 
            
            System.out.print("New data in Array: ");
            for (int i = 0; i < n; i++) {
                System.out.print(arr[i] + " ");
            }
            System.out.println();
        }
        
        user.close();
    }
}

    

