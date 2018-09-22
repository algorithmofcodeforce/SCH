package No1934;

import java.util.Scanner;

public class No1934 {

	public static int gcd(int x, int y) {
		while(y > 0) {
			int tmp = y;
			y = x % y;
			x = tmp;
		}
		
		return x;
	}
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		int T = scanner.nextInt();
		
		for(int i = 0; i < T; i++) {
			int A = scanner.nextInt();
			int B = scanner.nextInt();
			
			int lcm = A * B / gcd(A, B);
			
			System.out.println(lcm);
		}
		
		scanner.close();
	}

}
