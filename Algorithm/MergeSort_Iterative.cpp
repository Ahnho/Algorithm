#include<iostream>

#define MAX_SIZE 100

using namespace std;
int count;

void merge_sort(int v[], int n);

int main(){
    int Testcase_num;
    cin >> Testcase_num;

    for(int i =0 ; i < Testcase_num ; i++){
        int n ;
        cin >> n;
        int a[n];
        count = 0;
        for(int j=0; j < n ; j++){
            int m ;
            cin >> m;
            a[j] = m;
        }
        merge_sort(a, n);
        cout << count << endl;
    }
    return 0 ;
}


void merge(int a[], int low, int mid, int high){
    int i, j, k;
    int tmp[MAX_SIZE];

    for(i=low; i<=high; i++)
        tmp[i] = a[i];

    i = k = low;
    j = mid+1;

    while(i<=mid && j<=high){
        count++;
        if(tmp[i] <= tmp[j])
            a[k++] = tmp[i++];
        else
            a[k++] = tmp[j++];
    }

    while(i<=mid)   
        a[k++] = tmp[i++];

    while(j<=high)
        a[k++] = tmp[j++];
}

void merge_sort(int v[], int n){
    int size = 1;

    while (size < n){
        for(int i=0; i < n ; i += 2*size){
            int low = i;
            int mid = low + size -1 ;
            int high = min(i+ 2*size -1,n-1);

            if(mid >= n-1) break;

            merge(v,low,mid,high);
        }
        size *= 2;
    }
}
