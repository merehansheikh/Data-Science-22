// Electronics.java (Subclass)
class Electronics extends BaseProduct {
    private int warranty;

    public Electronics(String name, double price, int stock, int warranty) throws ProductException {
        super(name, price, stock);
        this.warranty = warranty;
    }

    @Override
    public double calculatePrice() {
        return (price > 1000) ? price * 0.9 : price;
    }

    @Override
    public String getDetails() {
        return super.getDetails() + ", Warranty: " + warranty + " months";
    }
}