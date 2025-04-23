#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main(){
    int T;

    cin >> T;

    for(int rep_cnt = 0; rep_cnt < T; rep_cnt++){
        int N, K, W;
        int n, k;
        cin >> N >> K;

        vector<int> times(N + 1);
        vector<int> need_times(N + 1);
        vector<int> in_degree(N + 1, 0);
        vector<vector<int>> out_degree(N + 1);
        queue<int> need_visit;

        for(n = 1; n < N + 1; n++){
            int time;
            cin >> time;
            times[n] = time;
            need_times[n] = time;
        }

        for(k = 0; k < K; k++){
            int start, end;
            cin >> start >> end;
            in_degree[end] += 1;
            out_degree[start].push_back(end);
        }

        for(n = 1; n < N + 1; n++)
            if(in_degree[n] == 0)
                need_visit.push(n);

        cin >> W;

        while(!need_visit.empty()){

            int cur_node = need_visit.front();
            need_visit.pop();

            for(int next_node: out_degree[cur_node]){
                need_times[next_node] = max(need_times[next_node], times[next_node] + need_times[cur_node]);
                in_degree[next_node] --;
                if(in_degree[next_node] == 0)
                    need_visit.push(next_node);
            }
        }

        cout << need_times[W] << endl;
    }
}