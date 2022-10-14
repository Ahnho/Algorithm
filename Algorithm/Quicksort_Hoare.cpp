#include<iostream>
#define MAX_SIZE 1001

using namespace std;

void Quick_sort_hoare(int a[], int low, int high);
void Quick_sort_Lomuto(int a[], int low, int high);

int swap_Lomuto;
int compare_Lomuto;
int swap_hoare;
int compare_hoare;

int main(){
    int numcase;
    cin >> numcase;
    while(numcase--){
        int n;
        cin >> n;
        int a[MAX_SIZE] ,b[MAX_SIZE] ;
        swap_Lomuto = 0 ; 
        compare_Lomuto = 0;
        swap_hoare = 0 ; 
        compare_hoare = 0;
        for(int i = 0 ; i < n ; i++){
            int m ;
            cin >> m;
            a[i] = m;
            b[i] = m;
        }
        Quick_sort_Lomuto(a,0,n-1);
        Quick_sort_hoare(b,0,n-1);
        cout << swap_hoare << " " <<  swap_Lomuto << " " << compare_hoare  << " " << compare_Lomuto <<  endl;
    }
    return 0;
}


void swap(int a, int b){
    int temp = b;
    b = a;
    a = temp;
}

int partition_Lomuto(int a[],int low,int high){
    int pivot = a[low];
    int j = low ;
    int tmp;
    for(int i = low+1 ; i <= high; i++){
        compare_Lomuto++;
        if(a[i] < pivot){
            j++;
            tmp = a[i];
            a[i] = a[j];
            a[j] = tmp;
            swap_Lomuto++;
        }
    }
    int pivot_pos = j;
    tmp = a[low];
    a[low] = a[pivot_pos];
    a[pivot_pos] = tmp;
    swap_Lomuto++;
    return pivot_pos;
}

int partition_hoare(int a[],int low,int high){
    int pivot = a[low];
    int i = low - 1;
    int j = high + 1;
    int tmp;
    while(true){
        do{
            i++;
            compare_hoare++;
        } while(a[i] < pivot);

        do{
            j--;
            compare_hoare++;
        } while(a[j] >pivot);
        if (i < j) {
        tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
        swap_hoare++;
      }
      else return j;
    }
}



void Quick_sort_hoare(int a[], int low, int high){
    if( low >= high ) return;

    int p = partition_hoare(a,low,high);

    Quick_sort_hoare(a,low,p);
    Quick_sort_hoare(a,p+1,high);
}

void Quick_sort_Lomuto(int a[], int low, int high){
    if( low >= high ) return;

    int p = partition_Lomuto(a,low,high);

    Quick_sort_Lomuto(a,low,p-1);
    Quick_sort_Lomuto(a,p+1,high);
}