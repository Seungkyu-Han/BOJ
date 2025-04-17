#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    
    vector<vector<bool>> board(n, vector<bool>(m, false));
    for(int i = 0; i < puddles.size(); i++){
        int cur_m = puddles[i][0];
        int cur_n = puddles[i][1];
        board[cur_n - 1][cur_m - 1] = true;
    }
    vector<vector<int>> dp(n, vector<int>(m, 0));
    dp[0][0] = 1;
    
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(board[i][j] || (i == 0 && j == 0))
                continue;
            
            int cur_path = 0;
            if(i > 0){
                cur_path += dp[i - 1][j];
            }
            
            if(j > 0){
                cur_path += dp[i][j - 1];
            }
            
            dp[i][j] = cur_path % 1000000007;
        }
    }
    
    return dp[n - 1][m - 1] % 1000000007;
}