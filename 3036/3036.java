// Backjoon Online Judge No.3036
// Java

package problem;

import java.util.Scanner;

public class No3036 {

    static int gcd(int x, int y) {
        return (y > 0) ? gcd(y, x % y) : x;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int init = sc.nextInt();

        for (int i = 1; i < N; i++) {
            int ring = sc.nextInt();
            int d = gcd(init, ring);
            
            // C notation으로 출력하기
            System.out.format("%d/%d\n", init / d, ring / d);
        }
        sc.close();
    }

}
