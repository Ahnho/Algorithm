#include <iostream>

using namespace std;

#define MAX(a,b) ((a) > (b) ? (a) : (b))

int LCS(string a , string b, int m , int n);

int main(){
    int numcase;
    cin >> numcase;
    for(int i = 0 ; i < numcase ; i++){
        string q,p;
        cin >> q >> p;
        int m = q.size();
        int n = p.size();
        cout << LCS(q,p,m,n) << endl; 
    }
}

int LCS(string a , string b, int m ,int n){
    if( m == 0 || n == 0) return 0;
    else if(a[m-1] == b[n-1]) return 1+LCS(a,b,m-1,n-1);
    else{
        int q = LCS(a,b,m,n-1);
        int p = LCS(a,b,m-1,n);
        return MAX(q,p);
    }
}
