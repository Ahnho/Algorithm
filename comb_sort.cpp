#include <iostream>
// #include <cstdio>

#define MAX_SIZE 1000
void combSort(int a[], int n);
int main(){
    int numTestCases;
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i){
        int num;
        int a[MAX_SIZE];
        scanf("%d", &num);
        for (int j = 0; j < num; j++)
            scanf("%d", &a[j]);
        combSort(a, num);
    }
return 0;
}



/* comb sort 함수 */
void combSort(int a[], int n) {
    int countCmpOps = 0; // 비교 연산자 실행 횟수
    int countSwaps = 0;// swap 함수 실행 횟수
    // comb sort 알고리즘 구현
    int gap = n;
    float shrink = 1.3;
    int temp;
    bool sorted = false;


    while(sorted == false){
        gap /= shrink;
        if(gap <= 1){
            gap = 1;
            sorted = true;
        }

        int i = 0;
        while((i+gap) < n){
            countCmpOps += 1;
            if(a[i] > a[i+gap]){
                temp = a[i];
                a[i] = a[i+gap];
                a[i+gap] = temp;
                countSwaps += 1;
                sorted = false;
            }
            i += 1;
        }

    }

    printf("%d %d ", countCmpOps, countSwaps);
    printf("\n");
}