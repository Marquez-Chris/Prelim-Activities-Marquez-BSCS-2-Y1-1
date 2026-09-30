package com.mycompany.marquezmidtermact1;
import java.util.Scanner;
import java.util.Date;
import java.text.SimpleDateFormat;
import java.text.ParseException;

// The main public class matching the required file name
public class MarquezMidtermProj6 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
        sdf.setLenient(false); // Ensures strict valid date evaluation

        System.out.println("=== MarquezMidtermProj6: Student Registry System ===");

        // 1. Demonstrate Default Constructor first
        System.out.println("\n[Creating default student baseline...]");
        Student defaultStudent = new Student();
        printStudentDetails(defaultStudent, sdf);

        // 2. Gather Custom User Input for the Parameterized Constructor
        System.out.println("\n[Please enter custom student details]");
        
        System.out.print("Enter Student Number: ");
        String inputNo = scanner.nextLine();

        System.out.print("Enter Student Full Name: ");
        String inputName = scanner.nextLine();

        // Safe Date Evaluation Input Loop
        Date inputDob = null;
        while (inputDob == null) {
            System.out.print("Enter Date of Birth (DD/MM/YYYY): ");
            String dateStr = scanner.nextLine();
            try {
                inputDob = sdf.parse(dateStr);
            } catch (ParseException e) {
                System.out.println("Invalid date format! Please use DD/MM/YYYY carefully.");
            }
        }

        // Safe Integer & Integrity Evaluation Input Loop
        Student customStudent = null;
        while (customStudent == null) {
            System.out.print("Enter Entry Tariff Points (20 - 280): ");
            try {
                int inputPoints = Integer.parseInt(scanner.nextLine());
                
                // Attempt instantiation (Will throw IllegalArgumentException if out of bounds)
                customStudent = new Student(inputNo, inputName, inputDob, inputPoints);
                
            } catch (NumberFormatException e) {
                System.out.println("Invalid input type! Tariff points must be a valid whole number.");
            } catch (IllegalArgumentException e) {
                System.out.println("Integrity Check Failed: " + e.getMessage() + " Please try again.");
            }
        }

        // 3. Confirm Successful Instantiation Output
        System.out.println("\n[Successfully registered custom student record]");
        printStudentDetails(customStudent, sdf);

        // Output cumulative static tracker state
        System.out.println("\n-------------------------------------------");
        System.out.println("Total Registered Instances (noOfStudents): " + Student.getNoOfStudents());
        System.out.println("-------------------------------------------");

        scanner.close();
    }

    private static void printStudentDetails(Student student, SimpleDateFormat sdf) {
        System.out.println("ID Number:     " + student.getStudentNo());
        System.out.println("Full Name:     " + student.getStudentName());
        System.out.println("Birth Date:    " + sdf.format(student.getDateOfBirth()));
        System.out.println("Tariff Points: " + student.getTariffPoints());
    }
}

// Student class definition (package-private, non-public to coexist in the same file)
class Student {
    private static int noOfStudents = 0;

    private String studentNo;
    private String studentName;
    private Date dateOfBirth;
    private int tariffPoints;

    // Default Constructor
    public Student() {
        this.studentNo = "not known";
        this.studentName = "not known";
        this.tariffPoints = 20; 
        
        try {
            SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
            this.dateOfBirth = sdf.parse("01/01/1995");
        } catch (Exception e) {
            this.dateOfBirth = new Date(); 
        }
        noOfStudents++;
    }

    // Parameterized Constructor
    public Student(String studentNo, String studentName, Date dateOfBirth, int tariffPoints) {
        this.studentNo = studentNo;
        this.studentName = studentName;
        this.dateOfBirth = dateOfBirth;
        setTariffPoints(tariffPoints); // Triggers integrity check
        noOfStudents++;
    }

    // --- Getters and Setters ---
    public static int getNoOfStudents() { return noOfStudents; }
    public String getStudentNo() { return studentNo; }
    public void setStudentNo(String studentNo) { this.studentNo = studentNo; }
    public String getStudentName() { return studentName; }
    public void setStudentName(String studentName) { this.studentName = studentName; }
    public Date getDateOfBirth() { return dateOfBirth; }
    public void setDateOfBirth(Date dateOfBirth) { this.dateOfBirth = dateOfBirth; }
    public int getTariffPoints() { return tariffPoints; }

    public void setTariffPoints(int tariffPoints) {
        if (tariffPoints >= 20 && tariffPoints <= 280) {
            this.tariffPoints = tariffPoints;
        } else {
            throw new IllegalArgumentException("Tariff points must fall inside the 20 to 280 bounds.");
        }
    }
}