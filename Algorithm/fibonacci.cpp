#include <iostream>
using namespace std;

int fibo(int n);

int main(){
    int numTestCases;
    cin >> numTestCases;
    for (int i = 0; i < numTestCases; ++i){
        int n;
        cin >> n;
        cout << fibo(n);
        printf("\n");
    }
    return 0;
}

int fibo(int n){
    if(n<=1)
        return n;
    else
        return fibo(n-1) + fibo(n-2);
}