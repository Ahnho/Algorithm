#include <iostream>

using namespace std;

void hanoi(int n , char q, char w, char e , int li[]);
int num;

int main(){
    int numTestCases;
    cin >> numTestCases;
    for (int i = 0; i < numTestCases; ++i){
        int n;
        cin >> n;
        num = 0;
        int li[n+1];
        hanoi(n,'a','b','c',li);
        printf("\n");
    }
    return 0;
}

void hanoi(int n , char q, char w, char e, int li[]){
    if (n>0){
        hanoi(n-1,q,e,w,li);
        if(q=='c'){
            li[num] = 0;
            num--;
            if (num == 0)
                cout << 0 << " " ;
            else
                cout << li[num] << " " ;
        }
        else if(e == 'c'){
            num++;
            li[num] = n;
            cout << li[num]  << " " ;
        }
        hanoi(n-1,w,q,e,li);
    }
}
