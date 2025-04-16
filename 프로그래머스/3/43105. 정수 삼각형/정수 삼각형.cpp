#include <string>
#include <vector>
#include <iostream>
#include <unordered_set>

using namespace std;

int solution(vector<vector<int>> triangle) {
    int answer = 0;
    vector<vector<int>> dp(triangle.size(), vector<int>(triangle.size(), 0));
    
    dp[0][0] = triangle[0][0];
    
    for(int i = 1; i < triangle.size(); i++){
        for(int j = 0; j < triangle[i].size(); j++){
            if(j == 0){
                dp[i][j] = dp[i - 1][0] + triangle[i][0];
            }
            else if(j == triangle[i].size() - 1){
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j];
            }
            else{
                int tmp = triangle[i][j];
                if(dp[i - 1][j - 1] > dp[i - 1][j]){
                    tmp += dp[i - 1][j - 1];
                }
                else{
                    tmp += dp[i - 1][j];
                }
                dp[i][j] = tmp;
            }
        }
    }
    
    for(int i = 0; i < triangle.size(); i++){
        if(answer < dp[dp.size() - 1][i])
            answer = dp[dp.size() - 1][i];
    }
    
    return answer;
}