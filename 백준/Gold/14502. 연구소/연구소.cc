#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int bfs(vector<vector<int>> board, int N, int M){

    vector<vector<bool>> visited(N, vector<bool>(M, false));

    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            if(visited[i][j] || board[i][j] != 2)
                continue;

            vector<pair<int, int>> need_visit;
            need_visit.emplace_back(i, j);

            while (!need_visit.empty()){
                pair<int, int> cur_pos = need_visit.back();
                need_visit.pop_back();

                for(int d = 0; d < 4; d++){
                    int next_n = cur_pos.first + dx[d], next_m = cur_pos.second + dy[d];
                    if(0 <= next_n && next_n < N && 0 <= next_m && next_m < M && !visited[next_n][next_m] && board[next_n][next_m] == 0){
                        board[next_n][next_m] = 2;
                        visited[next_n][next_m] = true;
                        need_visit.emplace_back(next_n, next_m);
                    }
                }
            }
        }
    }

    int result = 0;

    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++)
            if(board[i][j] == 0) result++;
    }

    return result;
}

int back_tracking(vector<vector<int>> &board, int construct_wall, int cur_n, int cur_m, int N, int M){
    if(construct_wall == 0){
        return bfs(board, N, M);
    }

    int result = 0;

    for(int i = cur_n; i < N; i++){
        for(int j = (i == cur_n) ? cur_m : 0; j < M; j++){
            if(board[i][j] == 0) {
                board[i][j] = 1;
                result = max(result, back_tracking(board, construct_wall - 1, i, j, N, M));
                board[i][j] = 0;
            }
        }
    }
    return result;
}

int main(){
    int N, M;
    cin >> N >> M;

    vector<vector<int>> board(N, vector<int>(M, 0));

    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            cin >> board[i][j];
        }
    }

    cout << back_tracking(board, 3, 0, 0, N, M) << endl;
}