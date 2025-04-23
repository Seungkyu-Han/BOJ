#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int N, K;

    cin >> N >> K;

    vector<int> dp(K + 1, 0);

    for(int i = 0; i < N; i++){
        int W, V;

        cin >> W >> V;

        for(int ii = K; ii >= W; ii--){
            dp[ii] = max(dp[ii], dp[ii - W] + V);
        }
    }

    cout << dp.back();
}