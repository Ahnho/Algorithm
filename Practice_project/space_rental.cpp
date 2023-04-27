#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

vector<int> get_f(vector<int> v) {
    int tmp = 0;
    for (size_t i = 0; i < v.size() - 1; i++) {
        if (!tmp) tmp = gcd(v[i], v[i + 1]);
        else tmp = gcd(tmp, v[i + 1]);
    }
    vector<int> ret;
    for (int i = 1; i <= tmp; i++) if (tmp % i == 0) ret.push_back(i);
    return ret;
}

int main() {
    int num_case;
    cin >> num_case;

    while (num_case--) {
        int n, t;
        cin >> n >> t;
        vector<pair<int, int>> info;
        vector<int> arg;
        for (int i = 0; i < n; i++) {
            int time, price;
            cin >> time >> price;
            info.push_back(make_pair(time, price));
            arg.push_back(price);
        }
        vector<int> f = get_f(arg);
        sort(info.begin(), info.end());
        vector<pair<int, int>> ct;
        for (size_t i = 0; i < f.size(); i++) {
            int point = 0;
            for (size_t j = 0; j < info.size(); j++) {
                if (info[j].second <= f[i]) continue;
                point = info[j].first;
                break;
            }
            for (int j = 1; j <= point; j++) {
                bool can = true;
                for (size_t k = 0; k < info.size(); k++) {
                    int cost = ((info[k].first / j) + 1) * f[i];
                    if (cost == info[k].second) continue;
                    can = false;
                    break;
                }
                if (can) ct.push_back(make_pair(j, f[i]));
            }
        }

        long long mn = LLONG_MAX;
        long long mx = 0;
        for (size_t i = 0; i < ct.size(); i++) {
            mx = max(mx, (t / static_cast<long long>(ct[i].first) + 1) * ct[i].second);
            mn = min(mn, (t / static_cast<long long>(ct[i].first) + 1) * ct[i].second);
        }
        if (ct.empty()) cout << -1 << '\n';
        else cout << mn << " " << mx << '\n';
    }

    return 0;
}
