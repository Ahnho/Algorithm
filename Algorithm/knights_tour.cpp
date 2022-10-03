#include <iostream>

using namespace std;


#define MARK 1
#define UNMARK 0 

typedef struct Point {int x,y;} point;

point direction[8] = {{1,-2},{2,-1},{2,1},{1,2},
                        {-1,2}, {-2,1},{-2,-1},{-1,-2}};


int board[9][9], path[9][9];

int knight(int m,int n,point pos, int cnt);

int main(){
    int numTestCases;
    cin >> numTestCases;
    for (int i = 0; i < numTestCases; ++i){
        int m,n,s,t;
        int count = 1;
        cin >> m >> n >> s >> t;
        board[m][n],  path[m][n];
        point p ;
        p.x =t-1 ; p.y = s-1; 
        for (int i = 0; i < m; i++)
            for(int j = 0; j < n ;j++)
                board[i][j] = UNMARK;
                
        board[p.y][p.x]= MARK;
        path[p.y][p.x] = 1;        

        int bl = knight(m,n,p,count) ;
        if(bl == 1){
            cout << 1 << endl;
            for (int i = 0; i<m; i++){
                for(int j = 0; j<n ;j++)
                    cout << path[i][j] <<" " ;
                printf("\n");
        }
        }
        else 
            cout << 0 << endl;
         
    }
    return 0;
}

int knight(int m,int n,point pos,int count){
    int i;
    point next ;

    if(count == m*n){
        return 1;
   }
    for(int i = 0; i<8; i++){
        next.x = pos.x + direction[i].y;
        next.y = pos.y + direction[i].x;

        if(next.x >= 0 && next.x < n && 
            next.y >= 0 && next.y < m &&
            board[next.y][next.x] != MARK)
        {   
            board[next.y][next.x] = MARK;
            path[next.y][next.x] = count +1;

            if(knight(m,n,next,count+1))
                return 1;
            
           board[next.y][next.x] = UNMARK;
        }
    }
    return 0;
}
