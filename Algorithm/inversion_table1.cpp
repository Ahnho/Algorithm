#include <iostream>

using namespace std;

void table(int a[], int n);

int main(){
    int numcase;
    cin >> numcase;
    while(numcase--){
        int n ;
        cin >> n;
        int a[n];
        int b[n];
        for(int i = 0 ; i < n ; i++){
            int w ;
            cin >> w;
            a[i] = w;
        }
        table(a,n);
    }
}

void table(int a[], int n){
    int s ; 
    int cnt ;
    for(int i = 1 ; i <= n ; i++){
        cnt = 0;
        for(int j = 0 ; j < n ; j++){
            if(i == a[j]){
                s = j;
                break;
            }
        }
        for(int k = 0 ; k < s ; k++){
            if(a[k] > i) cnt++;
        }
        cout << cnt << " " ;
    }
    cout << endl;
}
