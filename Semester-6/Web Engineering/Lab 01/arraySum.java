import java.util.*;

public class arraySum{
	
	public static void main(String[] args){
		int[] a1 = {1,2,2,4,5,9,3};
		int even = 0;
		int odd = 0;
		Scanner in = new Scanner(System.in);
		System.out.print("Original Array : ");
		System.out.print("[");
		for (int i=0; i<a1.length; i++){
			System.out.print(a1[i]);
			System.out.print(" ");
			if ((a1[i])%2==0){
				even++;
			}
			else{
				odd++;

			}
		}
		
		System.out.println("]");
		
		
		System.out.print("Count of Even Numbers : ");
		System.out.println(even);
		
		System.out.print("Count of Odd Numbers : ");
		System.out.println(odd);
	}
}