import java.util.*;

class InsufficientFundsException extends Exception {
    public InsufficientFundsException(String message) {
        super(message);
    }
}

class BankAccount {
    private String accountNumber;
    private double balance;

    public BankAccount(String accountNumber, double balance) {
        this.accountNumber = accountNumber;
        this.balance = balance;
    }

    public void deposit(double amount) {
        balance += amount;
        System.out.println("Deposited: " + amount + " | New Balance: " + balance);
    }

    public void withdraw(double amount) throws InsufficientFundsException {
        if (amount > balance) {
            throw new InsufficientFundsException("Insufficient balance for withdrawal!");
        }
        balance -= amount;
        System.out.println("Withdrawn: " + amount + " | Remaining Balance: " + balance);
    }

    public static void main(String[] args) {
        BankAccount account = new BankAccount("123456789", 1000);
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.print("Enter amount to withdraw: ");
            double amount = scanner.nextDouble();
            account.withdraw(amount);
        } catch (InsufficientFundsException e) {
            System.out.println("Exception: " + e.getMessage());
        } finally {
            System.out.println("Transaction complete.");
            scanner.close();
        }
    }
}