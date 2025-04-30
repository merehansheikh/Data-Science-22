

class Lecturer extends Staff{
    private double sessionPay;
    private int sessionCount;

    public Lecturer(String fullName, String empId, String dept, double sessionPay, int sessionCount) {
        super(fullName, empId, dept);
        this.sessionPay = sessionPay;
        this.sessionCount = sessionCount;
    }

    @Override
    public double calculateSalary() {
        return sessionPay * sessionCount;
    }

    @Override
    public String toString(){
        return super.toString() + ", Position: Lecturer, Salary: " + calculateSalary();
    }
}
