package problem;

import java.util.Scanner;

public class No13241 {

	public static int gcd(int x, int y) {
		while (y > 0) {
			int tmp = y;
			y = x % y;
			x = tmp;
		}

		return x;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int A = sc.nextInt();
		int B = sc.nextInt();

		// 반드시 명시적 형변환을 해주어야 한다.
		long lcm = (long) A * B / gcd(A, B);
		
		System.out.println(lcm);

		sc.close();
	}
}
