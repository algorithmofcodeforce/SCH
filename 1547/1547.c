// Backjoon Online Judge No.1547
// C
#include<stdio.h>

// 포인터를 이용한 배열 값 Swap 함수
void swap(int* x, int*y){
    int tmp = *x;
    *x = *y;
    *y = tmp;
}

int main(void){
    int M = 0, X = 0, Y = 0;
    int cups[4] = {-1, 1, 0, 0};

    // 공이 증발하는 경우 -1 리턴
    int answer = -1;

    scanf("%d", &M);
    for(int i = 0; i < M; i++){
        scanf("%d %d", &X, &Y);

        // 같은 경우 계산 생략
        if(X != Y){
            swap(&cups[X], &cups[Y]);
        }
    }
    for(int i = 1; i < 4 ;i++){
        if(cups[i]>0){
            answer = i;
            break;
        }
    }
    printf("%d", answer);
    return 0;
}