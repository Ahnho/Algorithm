#include <iostream>

using namespace std;

int kaprekar(int a[] );
void div(int n, int a[], int len);

int count ;

int main(){
    int numTestCases;
    cin >> numTestCases;
    for(int i = 0 ; i < numTestCases ; i++){
        int n;
        int a[4];
        int len = 4;
        count = 0;
        cin >> n ;
        div(n, a , len);
        cout << kaprekar(a) << " " << count << endl;       
    }

    return 0;
}

void div(int n, int a[], int len){
    for(int i = 0 ; i < len; i++ ){
        a[i] = n%10;
        n /= 10;
    }

}

void sort(int a[],int len){
    int temp;
    int i,j;
    for(i = 1 ; i < len ; i++){
        for(j=i ; j > 0 && a[j-1] > a[j]; j--){
            temp = a[j];
            a[j] = a[j-1];
            a[j-1] = temp;
        }
    }
}

int alpha(int a[], int len){
    int total = 0;
    int m = 1;
    
    for(int k = 0 ; k < len ; k++){
        total += a[k] * m;
        m *= 10;
    }

    return total;
}

int beta(int a[], int len){
    int total = 0;
    int m = 1;
    for(int k = len-1 ; k >= 0 ; k--){
        total += a[k] * m;
        m *= 10;
    }
    return total;
}


int kaprekar(int a[] ){
    int al,be;
    int len = 4;
    for(int i = 0; i < 7 ; i++){
        sort(a,len);
        al = alpha(a,len);
        be = beta(a,len);
        int total = al - be;
        count++;
        if(total == 0 || total == 6174)
            return total;
        int toa = total;
        len = toa?0:1; while (toa) { len++, toa/=10 ;}
        div(total,a,len);

    }
    return 0;
}