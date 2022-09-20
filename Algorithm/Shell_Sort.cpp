#include <iostream>

#define MAX_SIZE 1000
void ShellSort(int a[], int n);

int main(){
    int numTestCases;
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i){
        int num;
        int a[MAX_SIZE];
        scanf("%d", &num);
        for (int j = 0; j < num; j++)
            scanf("%d", &a[j]);
        ShellSort(a, num);
    }
    return 0;
}


/* Shell Sort 함수 */
void ShellSort(int a[], int n){
    int countCmpOps = 0; // 비교 연산자 실행 횟수
    int countSwaps = 0; // swap 함수 실행 횟수

    // Shell sort 알고리즘 구현
    int shrinkRatio = 2;
    int gap = n/shrinkRatio;
    int temp,i,j;

    while(gap>0){
        for(i = gap ; i<n;i++){
            temp = a[i];
            for(j = i; (j >= gap) && (a[j-gap]>temp);j-=gap){
                a[j] = a[j-gap];
                countSwaps += 1;
                countCmpOps += 1;
            }
            a[j] = temp; 
            if(j >= gap)
                countCmpOps += 1;
        }
        gap /= shrinkRatio;
    }

    printf("%d %d ", countCmpOps, countSwaps);
    printf("\n");
}
