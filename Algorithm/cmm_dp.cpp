#include <iostream>

#define MIN(a, b) ((a) < (b) ? (a) : (b))

using namespace std;

int orm[101][101];
int m[101][101];
int d[102];

void cmm(int n);
void order(int i, int j);

int main(){
    int numcase; cin >> numcase;
    while(numcase--){
        int n; cin >> n;
        for(int j=0; j<=n; j++) cin >> d[j];

        cmm(n+1);
        order(1, n); cout << endl;

        cout << m[1][n] << endl;
    }
    return 0;
}

void cmm(int n){
    for(int diog=0; diog<n; diog++){
        for(int i=0; i<n-diog; i++){
            int j = i + diog;
            if(j==i) m[i][j] = 0;
            else {
                m[i][j] = 99999999;
                for(int k=i; k<j; k++){
                    if(m[i][j] > (m[i][k] + m[k+1][j]) + (d[i-1]*d[k]*d[j])) orm[i][j] = k;
                    m[i][j] = MIN(m[i][j], (m[i][k] + m[k+1][j]) + (d[i-1]*d[k]*d[j]));
                }
            }
        }
    }
}

void order(int i, int j){
    if(i == j) cout << "M" << i;
    else{
        int k = orm[i][j];
        cout << "(";
        order(i, k);
        order(k+1, j);
        cout << ")";
    }
}

