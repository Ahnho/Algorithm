#include<iostream>

using namespace std;

int scale(int a[], int n);
void balance(int diff);

int count ;
int weight[7] = {100,50,20,10,5,2,1};

int main(){
    int numcase ;
    cin >> numcase;
    while(numcase--){
        int n;
        cin >> n;
        int a[n];
        count = 0;
        for(int i = 0;i < n ;i++) cin >> a[i];
        int dif = scale(a,n);
        balance(dif);
        cout << count << endl;
    }
}

int scale(int a[], int n){
    int left = 0;
    int right = 0;
    for (int i = 0 ; i < n ; i++){
        if(left <= right) left += a[i];
        else right += a[i];
    }
    if(left > right) return left-right;
    return right-left;
}

void balance(int diff){
    if(diff == 0) return ;

    for(int i = 0 ;i < 7 ; i++){
        count += diff / weight[i];
        diff %= weight[i];
    }
}
