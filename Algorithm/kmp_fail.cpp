#include <iostream>
using namespace std;

int cnt;
int f[1001];
void fail(int n, string s);
int KMP(string s1, string s2);

int main() {
	int numcase;
	cin >> numcase;
	for(int i=0;i<numcase;i++) {
		string s1, s2;
		cin >> s1 >> s2;
		cnt = 0;
        int n = s1.length();
        for(int j=0;j<= n ;j++) f[j] = 0; 
        fail(n, s1);
        for(int k=0;k<n;k++) cout << f[k] << " ";
		cout << endl;
		cout << KMP(s2, s1) << endl;
	}
}


void fail(int n, string s) {
	int j = 0;
	for(int i=1;i<n;i++) {
		while (j > 0 && s[i] != s[j]) j = f[j-1];
		if (s[i] == s[j]) f[i] = ++j;
	}
}

int KMP(string s1, string s2) {
	int j=0;
	for(int i=0;i<s1.length();i++) {
		while(j>0 && s1[i] != s2[j]) j = f[j-1];
		if(s1[i] == s2[j]) {
			if(j == s2.length()-1) {
				cnt ++;
				j = f[j];
			} 
            else j++;
		}
	}
	return cnt;
}