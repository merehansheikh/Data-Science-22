// Books.java (Subclass)
class Books extends BaseProduct {
    private String author;

    public Books(String name, double price, int stock, String author) throws ProductException {
        super(name, price, stock);
        this.author = author;
    }

    @Override
    public double calculatePrice() {
        return (price > 50) ? price * 0.93 : price;
    }

    @Override
    public String getDetails() {
        return super.getDetails() + ", Author: " + author;
    }

}