#include <iostream>
// #include <cstdio>

#define MAX_SIZE 1000
void insertionSort(int a[], int n);

int main(){
    int numTestCases;
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i){
        int num;
        int a[MAX_SIZE];
        scanf("%d", &num);
        for (int j = 0; j < num; j++)
            scanf("%d", &a[j]);

        insertionSort(a, num);
    }
    return 0;
}

/* Insertion Sort 함수 */
void insertionSort(int a[], int n){
    int countCmpOps = 0; // 비교 연산자 실행 횟수
    int countSwaps = 0; // swap 함수 실행 횟수
    int temp,i,j;

    // insertion sort 알고리즘 구현
    // J.Bentley
    for(i = 1 ; i < n ; i++){
        for(j=i ; j > 0 && a[j-1] > a[j]; j--){
            temp = a[j];
            a[j] = a[j-1];
            a[j-1] = temp;
            countSwaps += 1;
            countCmpOps += 1;
        }
        if(j > 0)
            countCmpOps += 1;
    }
    // Improvement insertion sort
    // for(int i = 1 ; i < n ; i++){
    //     countCmpOps += 1;
    //     temp = a[i];
    //     for(int j=i ; j > 0 && a[j-1] > a[j]; j--)
    //         a[j] = a[j-1];
    //     a[i] = temp;
    //     countSwaps += 1;
    // }

    printf("%d %d ", countCmpOps, countSwaps);
    printf("\n");
}