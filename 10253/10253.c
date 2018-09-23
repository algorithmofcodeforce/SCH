// Backjoon Online Judge No.10253
// C
#include<stdio.h>

// 최대공약수를 구하는 함수
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
    int Xa = 0, Xb = 0;

    scanf("%d", &T);

    for(int i = 0; i < T; i++){
        int ta = 1, tb = 2;

        scanf("%d %d", &Xa, &Xb);
        
        while(Xa != 1){
        
            while(((double)ta / tb) > ((double)Xa / Xb)){
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
            if(gcd(Xa, Xb) != 1){
                int d = gcd(Xa, Xb);
                Xa /= d;
                Xb /= d;
            }
        }
        printf("%d\n", Xb);
    }
    return 0;
}