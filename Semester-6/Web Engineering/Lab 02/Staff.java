

abstract class Staff{
    protected String fullName;
    protected String empId;
    protected String dept;

    public Staff(String fullName, String empId, String dept){
        this.fullName = fullName;
        this.empId = empId;
        this.dept = dept;
    }

    public abstract double calculateSalary();

    @Override
    public String toString(){
        return "Name: " + fullName + "\nID: " + empId + "\nDepartment: " + dept;
    }
}
