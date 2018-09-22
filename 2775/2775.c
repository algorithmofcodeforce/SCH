// Backjoon Online Judge No.1934
// C
#include<stdio.h>
int main(void){
    int T = 0, k = 0, n = 0;
    int floor[15][15] = {{0,1,2,3,4,5,6,7,8,9,10,11,12,13,14}, {0},};
    
    // Floor 초기화
    for(int f = 1; f < 15; f++){
        for(int r = 1; r < 15; r++){
            floor[f][r] = floor[f-1][r] + floor[f][r-1];
        }
    }

    scanf("%d", &T);

    for(int i = 0; i < T; i++){
        scanf("%d", &k);
        scanf("%d", &n);
        printf("%d\n", floor[k][n]);
    }

    return 0;
}