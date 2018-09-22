// Backjoon Online Judge No.13241
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
    // 일반적으로 int자료형의 범위는 약 2.1*10^9이다.
    // 입력값의 최대 범위는 10^8으로 int로 처리한다.
    int A = 0, B = 0;

    // 큰 수를 다룰 수 있도록 ull로 선언하였다.
    unsigned long long int lcm = 0;

    scanf("%d %d", &A, &B);
    lcm = (unsigned long long)A * B / gcd(A, B);
    
    printf("%llu\n", lcm);

    return 0;
}