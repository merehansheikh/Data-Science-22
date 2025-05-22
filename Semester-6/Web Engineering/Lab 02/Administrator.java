

class Administrator extends Staff{
    private double basePay;
    private double extraBonus;

    public Administrator(String fullName, String empId, String dept, double basePay, double extraBonus) {
        super(fullName, empId, dept);
        this.basePay = basePay;
        this.extraBonus = extraBonus;
    }

    @Override
    public double calculateSalary() {
        return basePay + extraBonus;
    }

    @Override
    public String toString(){
        return super.toString() + ", Position: Administrator, Salary: " + calculateSalary();
    }
}