import java.util.Scanner;

class Student {
    private int rollno;
    private String name;
    private String email;
    private String address;

    // Default Constructor
    public Student() {
        this.rollno = 0;
        this.name = "";
        this.email = "";
        this.address = "";
    }

    // Parameterized Constructor
    public Student(int rollno, String name, String email, String address) {
        this.rollno = rollno;
        this.name = name;
        this.email = email;
        this.address = address;
    }

    // Copy Constructor (Cloning)
    public Student(Student s) {
        this.rollno = s.rollno;
        this.name = s.name;
        this.email = s.email;
        this.address = s.address;
    }

    // Setters
    public void setRollno(int rollno) {
        this.rollno = rollno;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    // Getters
    public int getRollno() {
        return rollno;
    }

    public String getName() {
        return name;
    }

    public String getEmail() {
        return email;
    }

    public String getAddress() {
        return address;
    }

    // Method to take input from user
    public void inputData() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Roll Number: ");
        this.rollno = sc.nextInt();
        sc.nextLine(); // Consume newline
        System.out.print("Enter Name: ");
        this.name = sc.nextLine();
        System.out.print("Enter Email: ");
        this.email = sc.nextLine();
        System.out.print("Enter Address: ");
        this.address = sc.nextLine();
    }

    // Method to display student details
    public void showData() {
        System.out.println("Roll No: " + rollno);
        System.out.println("Name: " + name);
        System.out.println("Email: " + email);
        System.out.println("Address: " + address);
    }
}

// Driver class
public class Driver {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Student[] students = new Student[5];

        // Input details for 5 students
        for (int i = 0; i < students.length; i++) {
            System.out.println("\nEnter details for Student " + (i + 1) + ":");
            students[i] = new Student();
            students[i].inputData();
        }

        // Display details of 5 students
        System.out.println("\nStudent Details:");
        for (int i = 0; i < students.length; i++) {
            System.out.println("\nStudent " + (i + 1) + ":");
            students[i].showData();
        }

        sc.close();
    }
}
