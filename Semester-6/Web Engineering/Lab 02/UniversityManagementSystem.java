import java.util.Scanner;
public class UniversityManagementSystem {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        Staff[] employees = new Staff[2];

        for (int index = 0; index < employees.length; index++){
            System.out.println("Enter the category of the Staff (Professor, Lecturer, Administrator, Research Assistant): ");
            String role = scanner.nextLine();
            System.out.println("Enter full name: ");
            String fullName = scanner.nextLine();
            System.out.println("Enter Staff ID: ");
            String empId = scanner.nextLine();
            System.out.println("Enter department name: ");
            String dept = scanner.nextLine();

            switch(role.toLowerCase()){
                case "professor":
                    System.out.println("Enter monthly pay: ");
                    double monthlyPay = scanner.nextDouble();
                    employees[index] = new Professor(fullName, empId, dept, monthlyPay);
                    break;
                case "lecturer":
                    System.out.println("Enter payment per session: ");
                    double sessionPay = scanner.nextDouble();
                    System.out.println("Enter total sessions conducted: ");
                    int sessionCount = scanner.nextInt();
                    employees[index] = new Lecturer(fullName, empId, dept, sessionPay, sessionCount);
                    break;
                case "admin":
                    System.out.println("Enter base salary: ");
                    double basePay = scanner.nextDouble();
                    System.out.println("Enter additional bonus: ");
                    double extraBonus = scanner.nextDouble();
                    employees[index] = new Administrator(fullName, empId, dept, basePay, extraBonus);
                    break;
                case "research assistant":
                    System.out.println("Enter stipend amount: ");
                    double stipendAmount = scanner.nextDouble();
                    System.out.println("Enter research funding: ");
                    double funding = scanner.nextDouble();
                    employees[index] = new ResearchAssistant(fullName, empId, dept, stipendAmount, funding);
                    break;
                
                default:
                    System.out.println("Invalid role. Please enter again.");
                    index--;
                    break;
            }
            scanner.nextLine();
        }
        System.out.println("\nEmployee Information and Salaries:");
        for (Staff emp : employees) {
            System.out.println(emp.toString());
        }
    }
}