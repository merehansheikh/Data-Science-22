public class AvgArgs {
    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Please provide two numbers.");
            return;
        }

        int num1 = Integer.parseInt(args[0]);
        int num2 = Integer.parseInt(args[1]);
        double average = (num1 + num2) / 2.0;
        System.out.println("Average: " + average);
    }
}
