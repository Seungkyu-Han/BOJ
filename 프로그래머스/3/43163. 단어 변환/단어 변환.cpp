#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <queue>

using namespace std;


int is_neighbor(string start, string end){
    int length = start.size();
    bool flag = false;
    for(int i = 0; i < length; i++){
        if (start[i] != end[i]){
            if(flag)
                return 0;
            flag = true;
        }
    }
    return 1;
}

int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    int length = words.size();
    int target_index = -1;
    vector<vector<int>> graph(length + 1, vector<int>(length + 1, 0));
    
    for(int i = 0; i < length + 1; i++){
        string start_string;
        if(i == 0)
            start_string = begin;
        else
            start_string = words[i - 1];
        for(int j = i + 1; j < length + 1; j++){
            string end_string = words[j - 1];
            int result = is_neighbor(start_string, end_string);
            graph[i][j] = result;
            graph[j][i] = result;
        }
        if(target == start_string)
            target_index = i - 1;
    }
    
    queue<int> need_visit;
    need_visit.push(0);
    vector<int> visited(length + 1, -1);
    visited[0] = 0;
    
    while (need_visit.size() > 0){
        
        int num = need_visit.front();
        need_visit.pop();
        
        for(int i = 0; i < length; i++){
            if(graph[num][i + 1] == 1 && (visited[i + 1] == -1 || visited[i + 1] > visited[num] + 1)){
                visited[i + 1] = visited[num] + 1;
                need_visit.push(i + 1);
            }
        }
    }
    
    
    if(target_index == -1)
        return 0;
    return max(0, visited[target_index + 1]);
}
