package problem;

import java.util.Scanner;

public class No1094 {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int Stick = 0, cnt = 0;
    int i = 6;

    int X = sc.nextInt();

    while (true) {
      if (Stick + Math.pow(2, i) > X) {
        i--;
      } else if (Stick == X) {
        break;
      } else {
        Stick += Math.pow(2, i);
        cnt++;
        i--;
      }
    }

    System.out.println(cnt);

    sc.close();

  }

}
