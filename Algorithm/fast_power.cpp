#include <iostream>

using namespace std;

int f_pow(int x, int n);

int main(){
    int numTestCases;
    cin >> numTestCases;
    for (int i = 0; i < numTestCases; ++i){
        int x,n;
        cin >> x >> n ;
        cout << f_pow(x, n);
        printf("\n");
    }
    return 0;
}

int f_pow(int x, int n){
    int y;

    if (n==0)
        return 1;
    else if (n%2 == 1){
        y = f_pow(x, (n-1)/2);
        return (x*y*y)%1000  ;
    }
    else{
        y = f_pow(x, n/2);
        return (y*y)%1000 ;
    }
}    