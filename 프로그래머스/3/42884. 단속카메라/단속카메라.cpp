#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<vector<int>> routes) {
    int answer = 0;
    int length = routes.size();
    
    sort(routes.begin(), routes.end(), [](const vector<int> a, const vector<int> b){
        return a[1] < b[1];
    });
    
    int pos = -30001;
    
    for(int i = 0; i < length; i++){
        if(pos < routes[i][0]){
            answer ++;
            pos = routes[i][1];
        }
    }

    return answer;
}