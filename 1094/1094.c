// Backjoon Online Judge No.1094
// C
#include<stdio.h>
#include<math.h>

int main(void){
    int Stick = 0, cnt = 0;
    int i = 6, X = 0;

    scanf("%d", &X);

    // 모든 Xcm은 서로 다른 막대의 조합으로 만들 수 있다.
    while(1){
        if(Stick + pow(2, i) > X){
            i--;
        }
        else if(Stick == X){
            break;
        }
        else{
            Stick += pow(2, i);
            cnt++;
            i--;
        }
    }

    printf("%d", cnt);

    return 0;
}