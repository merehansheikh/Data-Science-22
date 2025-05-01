// BaseProduct.java (Base Class Implementing Product)
abstract class BaseProduct implements Product {
    protected String name;
    protected double price;
    protected int stock;

    public BaseProduct(String name, double price, int stock) throws ProductException {
        if (price < 0) throw new ProductException("Price cannot be negative");
        if (stock < 0) throw new ProductException("Stock cannot be negative");
        this.name = name;
        this.price = price;
        this.stock = stock;
    }

    public boolean isAvailable() {
        return stock > 0;
    }
    
    @Override
    public String getDetails() {
        return "Name: " + name + ", Price: $" + price + ", Stock: " + stock;
    }
}