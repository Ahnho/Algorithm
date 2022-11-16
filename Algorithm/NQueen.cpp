#include <iostream>

using namespace std;

int A;
int N;
int col[17];

void n_queen(int row);

int main(){
    int n; cin >> n;
    for(int i=0; i<n; i++){
        cin >> N; 
        A = 0;
        for(int j=0; j<N; j++){
            col[0] = j;
            n_queen(0);
        }
    }
    return 0;
}

int is_promising(int row){
    int k = 0, promising = 1;

    while(k < row && promising){
        if(col[row] == col[k] || abs(col[row] - col[k]) == row - k) 
            promising = 0;
        k++;
    }
    return promising;
}


void n_queen(int row){
    int i;
    if(A != 0) return ;

    if(is_promising(row)){
        if(row == N-1){
            for(int i=0; i<N; i++) cout << col[i] + 1 << " ";
            cout << endl;
            A = 1;
        }
        else{
            for(i=0; i<N; i++){
                col[row+1] = i;
                n_queen(row+1);
            }
        }
    }
}

