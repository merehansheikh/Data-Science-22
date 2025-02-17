import java.util.*;

public class ArrayMinMax {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Enter the size of the array: ");
        int size = in.nextInt();

        int[] numbers = new int[size];

        System.out.println("Enter " + size + " numbers:");
        for (int i = 0; i < size; i++) {
            numbers[i] = in.nextInt();
        }

        System.out.print("Array elements: ");
        for (int num : numbers) {
            System.out.print(num + " ");
        }
        System.out.println();
		
        int max = numbers[0];
        int min = numbers[0];

        for (int i = 1; i < size; i++) {
            if (numbers[i] > max) {
                max = numbers[i]; 
            }
            if (numbers[i] < min) {
                min = numbers[i]; 
            }
        }

        System.out.println("Maximum number: " + max);
        System.out.println("Minimum number: " + min);

    }
}
