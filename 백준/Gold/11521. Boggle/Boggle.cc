#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

const int MAX = 8;

typedef struct{
    int y, x;
}Dir;

Dir moveDir[8] = { {1, 1}, {1, 0}, {1, -1}, {0, 1}, {0, -1}, {-1, 1}, {-1, 0}, {-1, -1} };

int W, D;

vector<pair<string, bool> > v; //word, searched?

string board[MAX];

bool visited[MAX][MAX];


bool hasWord(int idx, int y, int x, string s){

    //조건 만족
    if (idx == s.length())
        return true;
    visited[y][x] = true;

    bool flag = false;

    for (int i = 0; i < 8; i++){
        if (flag)
            break;

        int nextY = y + moveDir[i].y;
        int nextX = x + moveDir[i].x;
        if (0 <= nextY && nextY < D && 0 <= nextX && nextX < D && !visited[nextY][nextX])
        if (board[nextY][nextX] == 'q'){
            if (idx < s.length() - 1 && s[idx] == 'q' && s[idx + 1] == 'u')
                flag = hasWord(idx + 2, nextY, nextX, s);
            }
        else if (board[nextY][nextX] == s[idx])
            flag= hasWord(idx + 1, nextY, nextX, s);
    }
    visited[y][x] = false;

    return flag;
}
int main(void){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> W;
    for (int i = 0; i < W; i++){
        string temp;
        cin >> temp;
        v.push_back({temp, false});
    }
    while (1){
        cin >> D;
        if (D == 0) break;
        
        for (int i = 0; i < W; i++)
            v[i].second = false;
        for (int i = 0; i < D; i++)
            cin >> board[i];

        vector<string> result;

        for (int i = 0; i < W; i++){
            for(int j=0; j<D; j++)
                for (int k = 0; k < D; k++){
                    bool flag = false;
                    memset(visited, false, sizeof(visited));
                    if (board[j][k] == 'q'){
                        if (!v[i].second && v[i].first.length() >= 2 && v[i].first[0] == 'q' && v[i].first[1] == 'u')
                            flag= hasWord(2, j, k, v[i].first);
                        }
                    else if (!v[i].second && board[j][k] == v[i].first[0]) flag = hasWord(1, j, k, v[i].first);
                    if (flag){
                        v[i].second = true;
                        result.push_back(v[i].first);
                    }
                }
        }
        sort(result.begin(), result.end());
        for (int i = 0; i < result.size(); i++)
            cout << result[i] << "\n";

        cout << "-\n";
    }

    return 0;
}