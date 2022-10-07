#include<iostream>

using namespace std;

void mcss_kadane(int a[], int n, int head, int tail);

int main(){
    int Testcase_num;
    cin >> Testcase_num;

    for(int i =0 ; i < Testcase_num ; i++){
        int n;
        cin >> n ;
        int a[n];
        for(int j=0; j < n ; j++){
            int m ;
            cin >> m;
            a[j] = m;
        }
        mcss_kadane(a,n,0,n-1);
    }
    return 0;
}

void mcss_kadane(int a[], int n, int head, int tail){
    int i,j ;
    int maxsum = 0, thissum = 0 ;
    head = -1;
    tail = -1;

    for(int i = 0 ,j=0; j < n ;j++){
        thissum += a[j];

        if(thissum > maxsum){
            maxsum = thissum;
            head = i;
            tail = j;
            if(a[i] == 0) head++;
        }
        else if (thissum < 0){
            i = j+1;
            thissum = 0;
        }
    }
    cout << maxsum << " " << head << " " << tail << endl;
}