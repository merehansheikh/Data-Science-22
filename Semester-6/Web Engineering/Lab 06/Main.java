public class Main {
    public static void main(String[] args) {
        LibraryManager library = new LibraryManager();

        // Add multiple books
        library.addBook(100, "The Great Gatsby", "F. Scott Fitzgerald");
        library.addBook(101, "To Kill a Mockingbird", "Harper Lee");
        library.addBook(102, "1984", "George Orwell");

        // Display all books
        System.out.println("\nAll Books:");
        library.displayBooks();

        // Borrow a book
        System.out.println("\nBorrowing Book ID 101:");
        library.borrowBook(101);

        // Display all books after borrowing
        System.out.println("\nAll Books after borrowing:");
        library.displayBooks();

        // Return a book
        System.out.println("\nReturning Book ID 101:");
        library.returnBook(101);

        // Display all books after returning
        System.out.println("\nAll Books after returning:");
        library.displayBooks();

        // Save data to a file
        String filename = "library.dat";
        library.saveToFile(filename);

        // Clear the current library data to test loading
        System.out.println("\nClearing current library data.");
        library = new LibraryManager();

        // Load data from file
        library.loadFromFile(filename);

        // Display all books after loading
        System.out.println("\nAll Books after loading from file:");
        library.displayBooks();
    }
}
