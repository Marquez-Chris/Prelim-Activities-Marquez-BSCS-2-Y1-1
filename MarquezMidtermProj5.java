package com.mycompany.marquezmidtermact1;
public class MarquezMidtermProj5 {
    public static void main(String[] args) {
        int totalBlocks = 4; 


        for (int i = 0; i < totalBlocks; i++) {
            System.out.print("*");
            
            for (int j = 0; j < i; j++) {
                System.out.print("A*");
            }
            
            if (i < totalBlocks - 1) {
                System.out.print(" \n");
            }
        }
        System.out.println();
    }
}
