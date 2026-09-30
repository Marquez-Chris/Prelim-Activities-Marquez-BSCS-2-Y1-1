package com.mycompany.marquezmidtermact1;
import java.util.Arrays;
import java.util.Scanner;


public class MarquezProj2 {
    public static void main(String[] args) {
        Scanner ussr = new Scanner(System.in);
        int[] RArray = new int[8];


      
        System.out.print("Enter 8 integer numbers:");
        for (int i = 0; i < 8; i++) {
            System.out.print("Element " + (i + 1) + ": ");
            RArray[i] = ussr.nextInt();
        }


    
        int[] uniqueArray = Arrays.stream(RArray).distinct().toArray();


        System.out.print("\nOriginal Array: " + Arrays.toString(RArray));
        System.out.print("Array after removing duplicates: " + Arrays.toString(uniqueArray));


        if (uniqueArray.length < 2) {
            System.out.print("\nCannot find second largest or second smallest elements because there are less than 2 unique numbers.");
        } else {
            Arrays.sort(uniqueArray);


            int secondSmallest = uniqueArray[1];
            


            int secondLargest = uniqueArray[uniqueArray.length - 2];


            System.out.print("The second smallest element is: " + secondSmallest);
            System.out.print("The second largest element is: " + secondLargest);
        }


        ussr.close();
    }
}