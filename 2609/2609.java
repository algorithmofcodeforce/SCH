// Backjoon Online Judge No.2609
// Java

package problem;

import java.util.Scanner;

public class No2609{
    
    // 재귀gcd함수를 이용하였다.
    static int gcd(int x, int y){
        return (y > 0) ? gcd(y, x % y) : x;
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int A = 0, B = 0;
        A = sc.nextInt();
        B = sc.nextInt();

        System.out.println(gcd(A, B));
        System.out.print(A * B / gcd(A, B));
        
        sc.close();
    }
}