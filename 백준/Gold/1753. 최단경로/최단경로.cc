#include <iostream>
#include <vector>
#include <climits>
#include <queue>

using namespace std;

struct node_element{
    int node;
    int distance;
};

struct element_compare{
    bool operator()(const node_element node_element1, const node_element node_element2){
        return node_element1.distance > node_element2.distance;
    }
};

vector<int> dijkstra(vector<vector<pair<int, int>>> &graph, int V, int K)  {
    vector<int> distances(V + 1, INT_MAX);
    distances[K] = 0;

    priority_queue<node_element, vector<node_element>, element_compare> need_visit;
    need_visit.push({K, 0});

    while(!need_visit.empty()){
        node_element cur_element = need_visit.top();
        need_visit.pop();

        int cur_node = cur_element.node, cur_distance = cur_element.distance;

        if(distances[cur_node] < cur_distance)
            continue;

        for(pair<int, int> cur_pair: graph[cur_node]){
            int next_node = cur_pair.first, next_distance = cur_distance + cur_pair.second;
            if(distances[next_node] > next_distance){
                distances[next_node] = next_distance;
                need_visit.push({next_node, next_distance});
            }
        }
    }

    return distances;
}

int main(){
    int V, E, K;
    int i;

    cin >> V >> E;
    cin >> K;

    vector<vector<pair<int, int>>> graph(V + 1);

    for(i = 0; i < E; i++){
        int u, v, w;

        cin >> u >> v >> w;
        graph[u].push_back({v, w});
    }

    vector<int> distances = dijkstra(graph, V, K);

    for(i = 1; i < V + 1; i++){
        cout << ((distances[i] != INT_MAX)? to_string(distances[i]) : "INF") << endl;
    }
}