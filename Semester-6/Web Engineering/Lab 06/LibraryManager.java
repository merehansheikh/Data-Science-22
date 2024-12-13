import java.io.*;
import java.util.HashMap;

public class LibraryManager {
    private HashMap<Integer, Book> books;

    public LibraryManager() {
        books = new HashMap<>();
    }

    public void addBook(int id, String title, String author) {
        if (books.containsKey(id)) {
            System.out.println("Book with ID " + id + " already exists.");
        } else {
            books.put(id, new Book(id, title, author));
            System.out.println("Book added: " + title);
        }
    }

    public void borrowBook(int id) {
        Book book = books.get(id);
        if (book != null) {
            if (book.isAvailable()) {
                book.setAvailable(false);
                System.out.println("You have borrowed the book: " + book.getTitle());
            } else {
                System.out.println("Book is already borrowed.");
            }
        } else {
            System.out.println("Book with ID " + id + " does not exist.");
        }
    }

    public void returnBook(int id) {
        Book book = books.get(id);
        if (book != null) {
            if (!book.isAvailable()) {
                book.setAvailable(true);
                System.out.println("You have returned the book: " + book.getTitle());
            } else {
                System.out.println("Book was not borrowed.");
            }
        } else {
            System.out.println("Book with ID " + id + " does not exist.");
        }
    }

    public void displayBooks() {
        if (books.isEmpty()) {
            System.out.println("No books in the library.");
        } else {
            for (Book book : books.values()) {
                System.out.println(book);
            }
        }
    }

    public void saveToFile(String filename) {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(filename))) {
            oos.writeObject(books);
            System.out.println("Library data saved to " + filename);
        } catch (IOException e) {
            System.out.println("Error saving library data: " + e.getMessage());
        }
    }

    @SuppressWarnings("unchecked") // Suppresses the warning for type safety
    public void loadFromFile(String filename) {
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(filename))) {
            books = (HashMap<Integer, Book>) ois.readObject();
            System.out.println("Library data loaded from " + filename);
        } catch (IOException | ClassNotFoundException e) {
            System.out.println("Error loading library data: " + e.getMessage());
        }
    }
}
