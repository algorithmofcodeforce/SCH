// Backjoon Online Judge No.10253
// Java

package problem;

import java.util.Scanner;


// C로 입력한 코드를 인용하였다. 
public class No10253 {

    static int gcd(int x, int y) {
        while (y > 0) {
            int tmp = y;
            y = x % y;
            x = tmp;
        }
        return x;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = 0;
        int Xa = 0, Xb = 0;

        T = sc.nextInt();

        for (int i = 0; i < T; i++) {
            int ta = 1, tb = 2;

            Xa = sc.nextInt();
            Xb = sc.nextInt();

            while (Xa != 1) {

                while (((double) ta / tb) > ((double) Xa / Xb)) {
                    tb++;
                }

                // 백업
                int tmpX = Xb;

                // X를 t로 통분
                Xa *= tb;
                Xb *= tb;

                // 분자 계산
                Xa -= ta * tmpX;

                // X약분
                if (gcd(Xa, Xb) != 1) {
                    int d = gcd(Xa, Xb);
                    Xa /= d;
                    Xb /= d;
                }
            }
            System.out.println(Xb);
        }
        sc.close();
    }

}
