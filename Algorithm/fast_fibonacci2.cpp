#include <iostream>
using namespace std;

int fast_fibo(int n);

int main(){
    int numTestCases;
    cin >> numTestCases;
    for (int i = 0; i < numTestCases; ++i){
        int n;
        cin >> n;
        cout << fast_fibo(n);
        printf("\n");
    }
    return 0;
}

void mulp(int m[2][2],int n[2][2]){
      int a =  m[0][0]*n[0][0] + m[0][1]*n[1][0];
      int b =  m[0][0]*n[0][1] + m[0][1]*n[1][1];
      int c =  m[1][0]*n[0][0] + m[1][1]*n[1][0];
      int d =  m[1][0]*n[0][1] + m[1][1]*n[1][1];

      m[0][0] = a%1000;
      m[0][1] = b%1000;
      m[1][0] = c%1000;
      m[1][1] = d%1000;
}


void pow(int m[2][2], int n){
    if(n <= 1) return ;
    int f[2][2] = {{1,1},{1,0}};

    pow(m, n/2);
    
    mulp(m, m);

    if(n % 2 != 0)
        mulp(m, f);
}

int fast_fibo(int n){
    if(n == 0) return 0;

    int m[2][2] = {{1,1},{1,0}};
    pow(m,n-1);

    return m[0][0];
}

