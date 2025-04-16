#include <string>
#include <vector>
#include <iostream>
#include <unordered_set>

using namespace std;

int find_node(int node, vector<int>& parent){
    if(node != parent[node])
        parent[node] = find_node(parent[node], parent);
    return parent[node];
}


void union_node(int node1, int node2, vector<int>& parent, vector<int>& rank){
    int root1 = find_node(node1, parent);
    int root2 = find_node(node2, parent);
    
    if (rank[root1] > rank[root2]){
        parent[root2] = root1;
    }
    else{
        parent[root1] = root2;
        if(rank[root1] == rank[root2]){
            rank[root1] ++;
        }
    }
}

int solution(int n, vector<vector<int>> computers) {
    
    vector<int> rank(n, 0);
    vector<int> parent(n, 0);
    
    for(int i = 0; i < n; i++)
        parent[i] = i;
    
    unordered_set<int> connected;
    
    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            if(computers[i][j] == 0)
                continue;
            
            if(find_node(i, parent) != find_node(j, parent)){
                union_node(i, j, parent, rank);
            }
        }
    }
    
    for(int i = 0; i < n; i++){
        connected.insert(find_node(i, parent));
    }
    
    for (int val : connected) {
        cout << val << " ";
    }
    cout << endl;
    
    return connected.size();
}