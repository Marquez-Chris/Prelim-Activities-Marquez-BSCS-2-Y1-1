package com.mycompany.marquezmidtermact1;
import java.util.Scanner;
public class MarquezMidtermAct1 {

    public static void main(String[] args) {
        Scanner user = new Scanner(System.in);
        int[] arr = new int[10];
        int Countn = 0;
        int sumofp = 0;
        int countp = 0;

        System.out.println("Enter 10 Real Numbhers: ");
        for(int i = 0; i < 10; i++){
          arr[i] = user.nextInt();
        }
        
        
        for(int i = 0; i < 10; i++){
            if (arr[i] >= 0){
                sumofp += arr[i];
                countp +=1;
            }
        }
        for (int i = 0; i < 10; i++){
            if (arr[i] < 0){
              Countn += 1;  
              
            }
        }
        int Minval = arr[0];    
        for (int i = 0; i < 10; i++){
            if (arr[i] < Minval){
              Minval = arr[i];  
              
            }
        }
    int ave = sumofp / countp;
    System.out.println("The Sum of all the positive numbers: "+sumofp);
    System.out.println("The Average of all the positive numbers: "+countp);
    System.out.println("The number of negatives are: "+Countn);
    System.out.println("The minimum value is: "+Minval);
    
    
    }
    
    
}
