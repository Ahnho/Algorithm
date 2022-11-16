#include <iostream>

using namespace std;


int Bd[4][4];
int col[4][5];
int row[4][5];
int square[4][5];
int A;

int squ(int a, int b);

void dfs(int c);

int main(){
    int n; cin >> n;
    for(int i=0; i<n; i++){   
        for(int j=0; j<4; j++){
            for(int k=0; k<5; k++){
                col[j][k] = row[j][k] = square[j][k] = 0;
            }
        }
        for(int j=0; j<4; j++){
            for(int k=0; k<4; k++){
                cin >> Bd[j][k];
                if(Bd[j][k]){
                    row[j][Bd[j][k]] = 1;
                    col[k][Bd[j][k]] = 1;
                    square[squ(j,k)][Bd[j][k]] = 1;
                }
            }
        }
        A = 0;
        dfs(0);
    }
}

int squ(int a, int b){
    return a/2*2 + b/2;
}

void dfs(int count){    
    if(count == 16 && A == 0){
        for(int i=0; i<4; i++){
        for(int j=0; j<4; j++) cout << Bd[i][j] << " ";
        cout << endl;
    }
    A = 1;
    return ;
    }
    int x = count / 4;
    int y = count % 4;
    if(Bd[x][y] == 0){
        for(int i=1; i<5; i++){
            if(!row[x][i] && !col[y][i] && !square[squ(x, y)][i] && !A){
                row[x][i] = col[y][i] = square[squ(x, y)][i] = 1;
                Bd[x][y] = i;
                dfs(count + 1);
                Bd[x][y] = 0;
                row[x][i] = col[y][i] = square[squ(x, y)][i] = 0;
            }
        }
    }
    else dfs(count + 1);
}

