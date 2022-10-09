#include<iostream>

#define MAX_SIZE 100

using namespace std;
int count;

void merge_sort(int v[], int low, int hight);

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
        merge_sort(a, 0 , n-1);
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

void merge_sort(int v[], int low, int high){
    int mid;
    if(low == high)
        return; 

    mid = (low + high) / 2;

    merge_sort(v, low, mid);
    merge_sort(v, mid+1, high);
    merge(v, low, mid, high);
}