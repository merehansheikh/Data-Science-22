// Groceries.java (Subclass)
import java.time.LocalDate;

class Groceries extends BaseProduct {
    private LocalDate expirationDate;

    public Groceries(String name, double price, int stock, LocalDate expirationDate) throws ProductException {
        super(name, price, stock);
        if (expirationDate.isBefore(LocalDate.now())) throw new ProductException("Product is expired");
        this.expirationDate = expirationDate;
    }

    @Override
    public double calculatePrice() {
        return (stock > 5) ? price * 0.92 : price;
    }

    @Override
    public String getDetails() {
        return super.getDetails() + ", Expiration Date: " + expirationDate;
    }
}