// ProductManagementSystem.java (Driver Class)
import java.util.Scanner;
import java.time.LocalDate;

public class ProductManagementSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        try {
            System.out.println("Select Product Type: 1. Electronics 2. Clothing 3. Groceries 4. Books");
            int choice = scanner.nextInt();
            scanner.nextLine();
            
            System.out.print("Enter product name: ");
            String name = scanner.nextLine();
            
            System.out.print("Enter price: ");
            double price = scanner.nextDouble();
            
            System.out.print("Enter stock: ");
            int stock = scanner.nextInt();
            scanner.nextLine();
            
            BaseProduct product = null;
            
            switch (choice) {
                case 1:
                    System.out.print("Enter warranty (months): ");
                    int warranty = scanner.nextInt();
                    product = new Electronics(name, price, stock, warranty);
                    break;
                case 2:
                    System.out.print("Enter size (S/M/L/XL): ");
                    String size = scanner.next();
                    System.out.print("Enter material: ");
                    String material = scanner.next();
                    product = new Clothing(name, price, stock, size, material);
                    break;
                case 3:
                    System.out.print("Enter expiration date (YYYY-MM-DD): ");
                    String date = scanner.next();
                    product = new Groceries(name, price, stock, LocalDate.parse(date));
                    break;
                case 4:
                    System.out.print("Enter author name: ");
                    String author = scanner.next();
                    product = new Books(name, price, stock, author);
                    break;
                default:
                    System.out.println("Invalid choice.");
                    return;
            }
            
            if (product.isAvailable()) {
                System.out.println("Product Details: " + product.getDetails());
                System.out.println("Final Price after Discount: $" + product.calculatePrice());
            } else {
                System.out.println("Product is out of stock.");
            }
        } catch (ProductException e) {
            System.out.println("Error: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("Invalid input!");
        } finally {
            System.out.println("Product processing complete.");
            scanner.close();
        }
    }
}
