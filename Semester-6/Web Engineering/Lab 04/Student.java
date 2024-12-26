import java.util.*;

class InvalidMarksException extends Exception {
    public InvalidMarksException(String message) {
        super(message);
    }
}

class Student {
    private String name;
    private int marks;

    public Student(String name, int marks) {
        this.name = name;
        this.marks = marks;
    }

    public String assignGrade() throws InvalidMarksException {
        if (marks < 0 || marks > 100) {
            throw new InvalidMarksException("Marks must be between 0 and 100.");
        }
        if (marks >= 85) return "A";
        if (marks >= 70) return "B";
        if (marks >= 50) return "C";
        return "F";
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        try {
            System.out.print("Enter student name: ");
            String name = scanner.nextLine();
            System.out.print("Enter marks: ");
            int marks = scanner.nextInt();
            
            Student student = new Student(name, marks);
            System.out.println("Grade: " + student.assignGrade());
        } catch (InvalidMarksException e) {
            System.out.println("Exception: " + e.getMessage());
        } finally {
            System.out.println("Grade assigned successfully.");
            scanner.close();
        }
    }
}
