#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer;
    unordered_map<int, int> num_dict;
    
    priority_queue<int> max_heap;
    priority_queue<int> min_heap;
    
    
    for(int i = 0; i < operations.size(); i++){
        bool command = operations[i].substr(0, 1) == "I";
        int num = stoi(operations[i].substr(2));
        
        if(command){
            max_heap.push(num);
            min_heap.push(num * -1);
            
            if(num_dict.find(num) == num_dict.end())
                num_dict[num] = 1;
            else
                num_dict[num] ++;
        }
        else{
            if(num > 0){
                while(max_heap.size() > 0){
                    int num = max_heap.top();
                    max_heap.pop();
                    if(num_dict[num] > 0){
                        num_dict[num]--;
                        break;
                    }
                }
            }
            else{
                while(min_heap.size() > 0){
                    int num = min_heap.top() * -1;
                    min_heap.pop();
                    if(num_dict[num] > 0){
                        num_dict[num]--;
                        break;
                    }
                }
            }
        }
    }
    
    int min_value = 9999999;
    int max_value = -9999999;
    
    while (max_heap.size() > 0){
        int num = max_heap.top();
        max_heap.pop();
        if(num_dict[num] != 0){
            min_value = min(min_value, num);
            max_value = max(max_value, num);
            break;
        }
    }
    
    while (min_heap.size() > 0){
        int num = min_heap.top() * -1;
        min_heap.pop();
        if(num_dict[num] != 0){
            min_value = min(min_value, num);
            max_value = max(max_value, num);
            break;
        }
    }
    
    if(max_value != -9999999)
        return {max_value, min_value};
    else
        return {0, 0};
}