import javax.swing.JOptionPane;

// Base class: Shape
class Shape {
    protected double area;
    protected double volume;

    // Default Constructor
    public Shape() {
        this.area = 0.0;
        this.volume = 0.0;
    }

    // Parameterized Constructor
    public Shape(double area, double volume) {
        this.area = area;
        this.volume = volume;
    }

    // Copy Constructor
    public Shape(Shape s) {
        this.area = s.area;
        this.volume = s.volume;
    }

    // Method to get input from the user (To be overridden)
    public void getInput() {
        this.area = Double.parseDouble(JOptionPane.showInputDialog("Enter Area:"));
        this.volume = Double.parseDouble(JOptionPane.showInputDialog("Enter Volume:"));
    }

    // Overriding toString() method to display details
    @Override
    public String toString() {
        return "Area: " + area + "\nVolume: " + volume;
    }
}

// Subclass: Square
class Square extends Shape {
    private double width;
    private double length;
    private double height;

    // Default Constructor
    public Square() {
        super();
        this.width = 0.0;
        this.length = 0.0;
        this.height = 0.0;
    }

    // Parameterized Constructor
    public Square(double width, double length, double height) {
        super(width * length, width * length * height); // Area = w*l, Volume = w*l*h
        this.width = width;
        this.length = length;
        this.height = height;
    }

    // Copy Constructor
    public Square(Square s) {
        super(s);
        this.width = s.width;
        this.length = s.length;
        this.height = s.height;
    }

    // Overriding getInput()
    @Override
    public void getInput() {
        width = Double.parseDouble(JOptionPane.showInputDialog("Enter Width:"));
        length = Double.parseDouble(JOptionPane.showInputDialog("Enter Length:"));
        height = Double.parseDouble(JOptionPane.showInputDialog("Enter Height:"));

        // Calculating area and volume
        area = width * length;
        volume = width * length * height;
    }

    // Overriding toString()
    @Override
    public String toString() {
        return "Square Details:\nWidth: " + width + "\nLength: " + length + "\nHeight: " + height +
               "\n" + super.toString();
    }
}

/// Subclass: Sphere
class Sphere extends Shape {
    private double radius;
    private static final double PI = 3.14; // ✅ STATIC so it's available before constructor execution

    // Default Constructor
    public Sphere() {
        super();
        this.radius = 0.0;
    }

    // Parameterized Constructor
    public Sphere(double radius) {
        super(4 * PI * radius * radius, (4 / 3.0) * PI * radius * radius * radius); // ✅ No error now
        this.radius = radius;
    }

    // Copy Constructor
    public Sphere(Sphere s) {
        super(s);
        this.radius = s.radius;
    }

    // Overriding getInput()
    @Override
    public void getInput() {
        radius = Double.parseDouble(JOptionPane.showInputDialog("Enter Radius:"));

        // Calculating area and volume
        area = 4 * PI * radius * radius;
        volume = (4 / 3.0) * PI * radius * radius * radius;
    }

    // Overriding toString()
    @Override
    public String toString() {
        return "Sphere Details:\nRadius: " + radius + "\n" + super.toString();
    }
}

// Driver Class
public class Driver2 {
    public static void main(String[] args) {
        // Creating an array to store Shape objects
        Shape[] shapes = new Shape[3];

        // Creating objects and getting user input
        shapes[0] = new Square();
        shapes[0].getInput();

        shapes[1] = new Sphere();
        shapes[1].getInput();

        shapes[2] = new Square(4, 5, 6); // Using parameterized constructor for one object

        // Displaying shape details
        for (Shape shape : shapes) {
            JOptionPane.showMessageDialog(null, shape.toString());
        }
    }
}

