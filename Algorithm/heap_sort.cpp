#include <iostream>

using namespace std;

int swp;
int heap[2002];
int heapSort(int n);
void fixHeap(int root, int k, int size);
void init() ;

int main() {
	int numcases, i, j;
	cin >> numcases;
	for(i=0;i<numcases;i++) {
		int n ; cin >> n;
		init();
		swp = 0;
		for(j=1;j<=n;j++) cin >> heap[j];
		cout << heapSort(n) << endl;
	}
	return 0;
}

void init() {
	for(int i=0;i<2002;i++) heap[i] = 0;
}

int heapSort(int n) {
	int i;
	for(i=n/2;i>=1;i--) fixHeap(i, heap[i], n);
	for(i=n;i>=2;i--) {
		int m = heap[1];
		fixHeap(1, heap[i], i-1);
		heap[i] = m;
	}
	return swp;
}

void fixHeap(int root, int k, int n) {
	int vc = root;
	int lc;

	while((heap[vc*2]!=0 && vc*2 <= n) || (heap[vc*2+1]!=0 && vc*2+1 <= n)){
		if(heap[vc*2+1] != 0 && vc*2+1 <= n) {
			swp = swp + 2;
			if(heap[vc*2] > heap[vc*2+1]) lc = vc*2;
			 else lc = vc*2+1;
		} 
        else {
			swp ++;
			lc = vc*2;
		}
		if(k < heap[lc]) {
			heap[vc] = heap[lc];
			vc = lc;
		} 
        else break;
	}
	heap[vc] = k;
}
