// Backjoon Online Judge
// C
#include<stdio.h>

// gcd함수를 재귀로 구현해보았다.
int gcd(int x, int y){
    return (y > 0) ? gcd(y, x % y) : x;
}

int main(void){
    int A = 0, B = 0;
    scanf("%d %d", &A, &B);

    printf("%d\n%d", gcd(A, B), (A * B / gcd(A, B)));
    return 0;
}