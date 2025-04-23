#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int T;
    cin >> T;
    for(int t = 0; t < T; t++){
        int N, n;
        cin >> N;
        vector<int> friends(N);
        vector<bool> success(N, false);

        for(n = 0; n < N; n++){
            int wanted_friend;
            cin >> wanted_friend;
            friends[n] = wanted_friend - 1;
        }

        vector<int> visited(N + 1, false);

        for(n = 0; n < N; n++){
            if(visited[n])
                continue;

            int cur_node = n;
            vector<int> path;

            while(!visited[cur_node]){
                path.push_back(cur_node);
                visited[cur_node] = true;
                cur_node = friends[cur_node];
            }

            bool flag = false;

            for(int node: path){
                if(flag)
                    success[node] = true;
                else if(node == cur_node){
                    flag = true;
                    success[node] = true;
                }
            }
        }

        int result = 0;
        for(bool is_success: success)
            if(!is_success) result++;
        cout << result << endl;
    }
}