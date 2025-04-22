#include <iostream>
#include <queue>
#include <set>

using namespace std;

void dfs(const vector<set<int>> &graph, int N, int V){
    vector<int> need_visit;
    need_visit.push_back(V);

    vector<bool> visited(N + 1, false);

    while(!need_visit.empty()){

        int cur_node = need_visit.back();
        need_visit.pop_back();

        if (visited[cur_node])
            continue;

        cout << cur_node << " ";
        visited[cur_node] = true;

        vector<int> to_reverse;
        for(int next_node: graph[cur_node]){
            if(!visited[next_node])
                to_reverse.push_back(next_node);
        }

        while(!to_reverse.empty()){
            int reversed_node = to_reverse.back();
            to_reverse.pop_back();

            need_visit.push_back(reversed_node);
        }
    }
    cout << endl;
}

void bfs(const vector<set<int>> &graph, int N, int V){
    queue<int> need_visit;
    need_visit.push(V);

    vector<bool> visited(N + 1, false);

    while(!need_visit.empty()){
        int cur_node = need_visit.front();
        need_visit.pop();

        if(visited[cur_node])
            continue;

        cout << cur_node << " ";
        visited[cur_node] = true;

        for(int next_node: graph[cur_node]){
            if(!visited[next_node])
                need_visit.push(next_node);
        }
    }
}

int main(){
    int N, M, V;

    cin >> N >> M >> V;

    vector<set<int>> graph(N + 1);

    for(int i = 0; i < M; i++){
        int node1, node2;
        cin >> node1 >> node2;
        graph[node1].insert(node2);
        graph[node2].insert(node1);
    }

    dfs(graph, N, V);
    bfs(graph, N, V);
}