#include <iostream>

using namespace std;

int gcd(int a, int b);

int main(){
    int numTestCases;
    cin >> numTestCases;
    for (int i = 0; i < numTestCases; ++i){
        int a,b;
        cin >> a;
        cin >> b;
        cout << gcd(a, b);
        printf("\n");
    }
    return 0;
}

int gcd(int a, int b){
    if(b == 0)
        return a;
    else
        return gcd(b, a%b);
}