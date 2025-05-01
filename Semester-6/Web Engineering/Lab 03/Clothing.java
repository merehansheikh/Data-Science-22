// Clothing.java (Subclass)
class Clothing extends BaseProduct {
    private String size;
    private String material;

    public Clothing(String name, double price, int stock, String size, String material) throws ProductException {
        super(name, price, stock);
        this.size = size;
        this.material = material;
    }

    @Override
    public double calculatePrice() {
        return (stock < 5) ? price * 0.95 : price;
    }

    @Override
    public String getDetails() {
        return super.getDetails() + ", Size: " + size + ", Material: " + material;
    }
}
