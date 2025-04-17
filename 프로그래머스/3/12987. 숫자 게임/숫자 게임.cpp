#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int solution(vector<int> A, vector<int> B) {
    int answer = 0;
    int length = A.size();
    
    sort(A.begin(), A.end(), greater<int>());
    sort(B.begin(), B.end(), greater<int>());
    
    int a_index = 0, b_index = 0;
    
    while(a_index < length && b_index < length){
        if(A[a_index] >= B[b_index])
            a_index++;
        else{
            a_index++;
            b_index++;
            answer++;
        }
    }
    
    return answer;
}