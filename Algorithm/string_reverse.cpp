#include <iostream>

using namespace std;

string reverse(string &a, int h, int n);

int main(){
    int numTestCases;
    cin >> numTestCases;
    for (int i = 0; i < numTestCases; ++i){
        string st;
        cin >> st;
        int n = st.length()-1;
        int h = 0;
        cout << reverse(st,h, n);
        printf("\n");
    } 
    return 0;
}



string reverse(string &a, int h ,int n){
    char temp;
    if(h < n){
        temp = a[h];
        a[h] = a[n];
        a[n] = temp;
        reverse(a,h+1,n-1);
    }
    return a;
}

