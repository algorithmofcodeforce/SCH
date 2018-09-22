package problem;

import java.util.Scanner;

public class No2775 {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int T = 0, k = 0, n = 0;
    int floor[][] = new int[15][15];

    // 코드가 좀 더러운데 차차 배우겠지..?
    // Floor[0] 초기화
    for(int i = 0; i < 15; i++){
      floor[0][i] = i;
    }

    // 나머지 Floor 초기화
    for(int f = 1; f < 15; f++){
        for(int r = 1; r < 15; r++){
            floor[f][r] = floor[f-1][r] + floor[f][r-1];
        }
    }

    T = sc.nextInt();

    for(int i = 0; i < T; i++){
        k = sc.nextInt();
        n = sc.nextInt();
        System.out.println(floor[k][n]);
    }

    sc.close();

  }

}
