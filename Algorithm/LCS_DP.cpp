#include <iostream>

using namespace std;

#define MAX_LENGTH 101
#define MAX(a,b) ((a) > (b) ? (a) : (b))

int L[MAX_LENGTH][MAX_LENGTH], S[MAX_LENGTH][MAX_LENGTH];

int LCS(char a[], char b[], int m, int n);
void printLCS(char s[], char t[], int m, int n);

int main(){
    int numcase;
    cin >> numcase;
    for(int i = 0 ; i < numcase ; i++){
        string q,p;
        cin >> q >> p;
        int m = q.size();
        int n = p.size();
        char a[m];
        char b[n];
        for(int i = 0 ; i < m ; i++) a[i] = q[i];
        for(int i = 0 ; i < n ; i++) b[i] = p[i];
        cout << LCS(a,b,m,n) << " " ;
        printLCS(a,b,m,n);
        cout << endl;
    }
}

int LCS(char a[], char b[], int m, int n){
    int i,j; 

    for(i = 0; i <= m; i++) L[i][0] = 0;
    for(i = 0; i <= n; i++) L[0][i] = 0;

    for(i = 1; i <= m; i++){
        for(j = 1; j <= n; j++){
            if (a[i-1] == b[j-1]){
                L[i][j] = L[i-1][j-1]+1;
                S[i][j] = 0;
            }
            else{
                L[i][j] = MAX(L[i][j-1], L[i-1][j]);
                if (L[i][j] == L[i][j-1]) S[i][j] = 1;
                else S[i][j] = 2;
            }
        }
    }
    return L[m][n];
}

void printLCS(char s[], char t[], int m, int n){
    if(m==0 || n==0) return;
    if(S[m][n] == 0){
        printLCS(s, t, m-1, n-1);
        printf("%c", s[m-1]);
    }
    else if(S[m][n] == 1) printLCS(s, t, m, n-1);
    else if(S[m][n] == 2) printLCS(s, t, m-1, n);
}
