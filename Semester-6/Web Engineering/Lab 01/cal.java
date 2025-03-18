import java.util.*;

public class cal{

    public static void main(String[] args) {
		int val1, val2;
		Scanner in = new Scanner(System.in);
		System.out.println("Please Enter Value 1 : ");
		val1 = in.nextInt();
		System.out.println("Please Enter Value 2 : ");
		val2 = in.nextInt();
		
		int result=0;
		if (args[0].equals("+")){
			result = val1+val2;	
		}
		if (args[0].equals("-")){
			result = val1-val2;
		}
		if (args[0].equals("*")){
			result = val1*val2;
		}
		if (args[0].equals("/")){
			result = val1/val2;
		}
		System.out.println("Result : ");
		System.out.println(result);
	}
}
		
