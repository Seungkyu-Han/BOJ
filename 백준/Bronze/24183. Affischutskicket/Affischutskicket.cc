#include <bits/stdc++.h>

#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
using namespace std;

int DB[] = {229 * 324, 297 * 420, 210 * 297}, v[3];

int main() {
    fastio;
    cin >> v[0] >> v[1] >> v[2];
    cout << fixed << setprecision(6) << (2 * v[0] * DB[0] + 2 * v[1] * DB[1] + v[2] * DB[2]) * 1e-6;
    return 0;
}