#include <iostream>

#define MIN(a, b) ((a) < (b) ? (a) : (b))

using namespace std;

int cmm_rc(int a[], int i, int j);

int main(){
    int numcase; 
    cin >> numcase;

    while(numcase--){
        int n; cin >> n;
        int a[n+1];
        for(int i=0; i<=n; i++) cin >> a[i];
        cout << cmm_rc(a, 1, n) << endl;
    }
    return 0;
}

int cmm_rc(int a[], int i, int j){
    int m, temp;
    if(i == j) return 0;
    m = 999999999;
    
    for(int k=i; k<j; k++){
        temp = cmm_rc(a, i, k) + cmm_rc(a, k+1, j) + (a[i-1] * a[k] * a[j]);
        m = MIN(m, temp);
    }
    return m;
}
