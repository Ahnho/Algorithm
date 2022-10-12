#include <iostream>
using namespace std;

int Golomb(int n);

int li[1001];

int main(){
    int numTestCases;
    cin >> numTestCases;
    while(numTestCases--){
        int n ;
        cin >> n;
        cout << Golomb(n) << endl;
    }
    return 0;
}

int Golomb(int n){
    li[1] = 1;
    int index = 1;
    int location = 1;
    while(location < n){
        index++;
		li[index] = 1 + li[index - li[li[index - 1]]]; 
		location += li[index];
    }
    return index;
}