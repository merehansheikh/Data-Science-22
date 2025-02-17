public class AnnualPayCalculator {

    public static void main(String[] args) {
        // Define variables
        double payAmount = 2000.00; 
        int payPeriods = 12;         
        double annualPay;             

        annualPay = payAmount * payPeriods;


        System.out.println("Employee's Total Annual Pay: $" + annualPay);
    }
}
