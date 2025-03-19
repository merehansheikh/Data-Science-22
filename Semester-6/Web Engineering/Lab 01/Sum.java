import java.util.*;

public class Sum{
	
	public static void main(String[] args){
		int val1 = 0, val2 = 0;
		int count = 0;
		Scanner in = new Scanner(System.in);
		Sum obj = new Sum();

		while (true){			
			System.out.println("Please Enter Value 1 : ");
			val1 = in.nextInt();
			if (val1 == -1) {
                break;
            }
			
			System.out.println("Please Enter Value 2 : ");
			val2 = in.nextInt();
			if (val2 == -1) {
                break;
            }
			
			if (val1 <= 0 || val2 <= 0) {
                System.out.println("Both numbers must be positive. Try again.");
                continue;
			}
			int result = obj.summ(val1,val2);
			count++;
			
			System.out.print("Sum is :");
			System.out.println(result);
			System.out.print("Operation performed : ");
			System.out.println(count);
		}
	}
	
	public int summ(int x, int y){
		int r = x+y;
		return r;
	}
}