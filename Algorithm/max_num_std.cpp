#include<iostream>

using namespace std;

# define MAX(a,b) ((a)>(b) ? (a):(b))

int max_num(int a[], int left, int right);

int main(){
    int Testcase_num;
    cin >> Testcase_num;

    for(int i =0 ; i < Testcase_num ; i++){
        int n ;
        cin >> n;
        int a[n];
        for(int j=0; j < n ; j++){
            int m ;
            cin >> m;
            a[j] = m;
        }
        cout << max_num(a, 0,n-1) << endl;
    }
}

int max_num(int a[], int left, int right){
    int half ;

    if (left == right) return a[left];

    else{
        half = (left + right)/2;
        left = max_num(a,left,half);
        right = max_num(a,half+1,right);
        return MAX(left,right);
    }
}