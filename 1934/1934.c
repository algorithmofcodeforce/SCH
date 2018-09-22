// Backjoon Online Judge No.1934
// C
#include<stdio.h>

int gcd(int x, int y){
    while(y > 0){
        int tmp = y;
        y = x % y;
        x = tmp;
    }
    return x;
}

int main(void){
    int T = 0;
    int A = 0, B = 0;
    int lcm = 0;

    scanf("%d", &T);

    for(int i = 0; i < T; i++){
        scanf("%d %d", &A, &B);
        lcm = A * B / gcd(A, B);
        printf("%d\n", lcm);
    }

    return 0;
}