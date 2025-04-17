#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> sticker)
{
    int answer = 0;
    int length = sticker.size();
    
    vector<int> use_0 = {0, sticker[0]};
    vector<int> use_1 = {0, 0};

    for(int i = 1; i < length - 1; i++){
        
        int length_0 = use_0.size();
        int length_1 = use_1.size();
        
        use_0.push_back(max(use_0.back(), use_0[length_0 - 2] + sticker[i]));
        use_1.push_back(max(use_1.back(), use_1[length_1 - 2] + sticker[i]));
    }
    
    int length_1 = use_1.size();
    use_1.push_back(max(use_1.back(), use_1[length_1 - 2] + sticker.back()));

    return max(use_0.back(), use_1.back());
}