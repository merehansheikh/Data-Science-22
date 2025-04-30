

class Professor extends Staff{
    private double monthlyPay;

    public Professor(String fullName, String empId, String dept, double monthlyPay) {
        super(fullName, empId, dept);
        this.monthlyPay = monthlyPay;
    }

    @Override
    public double calculateSalary() {
        return monthlyPay;
    }

    @Override
    public String toString(){
        return super.toString() + ", Position: Professor, Salary: " + calculateSalary();
    }
}