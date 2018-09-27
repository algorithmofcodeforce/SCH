// Backjoon Online Judge No.3036
// C
#include<stdio.h>

int gcd(int x, int y){
    return (y > 0) ? gcd(y, x % y) : x;
}

int main(void){
    int N = 0, BIG = 0, ring = 0, d = 0;

    scanf("%d", &N);
    scanf("%d", &BIG);

    for(int i = 1; i < N; i++){
        scanf("%d", &ring);
        d = gcd(BIG, ring);
        printf("%d/%d\n", BIG/d, ring/d);
    }
    return 0;
}