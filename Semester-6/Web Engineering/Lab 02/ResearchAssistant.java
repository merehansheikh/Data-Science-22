
class ResearchAssistant extends Staff{
    private double stipendAmount;
    private double funding;

    public ResearchAssistant(String fullName, String empId, String dept, double stipendAmount, double funding) {
        super(fullName, empId, dept);
        this.stipendAmount = stipendAmount;
        this.funding = funding;
    }

    @Override
    public double calculateSalary() {
        return stipendAmount + funding;
    }

    @Override
    public String toString(){
        return super.toString() + ", Position: Research Assistant, Salary: " + calculateSalary();
    }
}