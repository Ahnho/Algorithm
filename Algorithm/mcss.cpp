#include<iostream>
using namespace std;

int mcss(int a[], int left, int right);

int main(){
    int Testcase_num;
    cin >> Testcase_num;

    for(int i =0 ; i < Testcase_num ; i++){
        int n;
        cin >> n ;
        int a[n];
        for(int j=0; j < n ; j++){
            int m ;
            cin >> m;
            a[j] = m;
        }
        int answer = mcss(a,0,n-1);
        if (answer <= 0)  cout << 0 << endl;
        else cout << mcss(a,0,n-1) << endl;
    }
    return 0;
}

int max_3(int a, int b, int c){
    int m = max(a,b);
    return max(m,c);
}

int mid_mcss(int a[], int left,int mid, int right){
    int sum = 0;
    int left_sum = -1001;
    for (int i = mid; i >= left; i--) {
        sum +=  a[i];
        left_sum = max(sum,left_sum);
    }

    sum = 0 ;
    int right_sum = -1001;
    for (int k = mid; k <= right; k++) {
        sum += a[k];
        right_sum = max(sum,right_sum);
    }

    return max_3(left_sum + right_sum - a[mid], left_sum, right_sum);

}

int mcss(int a[], int left, int right){
    if(left > right) return -1;
    if (left == right) return a[left];

    int mid = (left + right)/2;

    int left_sum = mcss(a, left, mid-1);
    int right_sum = mcss(a,mid+1,right);
    int mid_sum = mid_mcss(a,left,mid,right);
    
    return max_3(left_sum,right_sum,mid_sum);
}