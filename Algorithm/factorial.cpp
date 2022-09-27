#include <iostream>
using namespace std;

int fac(int n);

int main(){
    int numTestCases;
    cin >> numTestCases;
    for (int i = 0; i < numTestCases; ++i){
        int n;
        cin >> n;
        cout << fac(n)%1000 ;
        printf("\n");
    }
    return 0;
}

int fac(int n){
    if(n <= 1)
        return 1;
    else{
        int num = n * fac(n-1);
        while (num % 10 == 0)
            num /= 10;
        return  num % 10000 ;
    }
}
