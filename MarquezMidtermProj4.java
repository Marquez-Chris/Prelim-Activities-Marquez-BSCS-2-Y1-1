
package com.mycompany.marquezmidtermact1;
import java.util.Scanner;


public class MarquezMidtermProj4 {
    public static void main(String[] args) {
        Scanner ussr = new Scanner(System.in);
        
        System.out.print("Enter Size of Array : ");
        int size = ussr.nextInt();
        
        int[] arr = new int[size];
        
        System.out.print("Enter any " + size + " elements in Array: ");
        for (int i = 0; i < size; i++) {
            arr[i] = ussr.nextInt();
        }
        
        System.out.print("Even Elements: ");
        for (int i = 0; i < size; i++) {
            if (arr[i] % 2 == 0) {
                System.out.print(arr[i] + " ");
            }
        }
        System.out.println(); 
        
        System.out.print("Odd Elements: ");
        for (int i = 0; i < size; i++) {
            if (arr[i] % 2 != 0) {
                System.out.print(arr[i] + " ");
            }
        }
        System.out.println();
        
        ussr.close();
    }
}
