#include <iostream>

using namespace std;

int permu(string &str, int begin, int end);
int count;

int main(){
    int numTestCases;
    cin >> numTestCases;
    for (int i = 0; i < numTestCases; ++i){
        string st;
        cin >> st;
        int n = st.length();
        count = 0;
        cout << permu(st,0,n);
        printf("\n");
        
    }
    return 0;
}

void swap(char* a, char* b){
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

int pow(int a, int b){
    int total = 1; 
    for(int i = 0 ; i < b ; i++ )
        total *= a;
    return total;
}

int weight(string &a, int n){
    int sum = 0;
    for(int i=0; i < n ; i++){
        sum += pow(-1,i) * (int(a[i]) - int('a')); 
    }
    return sum;
}


int permu(string &str, int begin, int end){
    int i;
    int range = end - begin;
    if(range == 1){
        if(weight(str,end) > 0)
            count++;
    }
    else{
        for(i=0; i<range;i++){
            swap(&str[begin], &str[begin+i]);
            permu(str,begin+1,end);
            swap(&str[begin], &str[begin+i]);
        }
    }
    return count;
}
