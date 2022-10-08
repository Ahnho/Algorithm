#include<iostream>

using namespace std;


int binary_search(int a[], int left, int right, int value);

int main(){
    int Testcase_num;
    cin >> Testcase_num;

    for(int i =0 ; i < Testcase_num ; i++){
        int n, value;
        cin >> n >> value;
        int a[n];
        for(int j=0; j < n ; j++){
            int m ;
            cin >> m;
            a[j] = m;
        }
        cout << binary_search(a,0,n-1,value) << endl;
    }
    return 0;
}

int binary_search(int a[], int left, int right, int value){
    int mid;
    if (left > right) return -1; 

    else{
        mid = (left+right)/2;
        if (a[mid] == value) return mid;
        else if (a[mid] > value) return binary_search(a, left, mid-1, value);
        else return binary_search(a, mid+1, right, value);
    }
}