import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {

    static int R, C;
    static char[][] board;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        R = sc.nextInt();
        C = sc.nextInt();
        sc.nextLine(); // 개행 문자 제거

        board = new char[R][C];
        for (int i = 0; i < R; i++) {
            board[i] = sc.nextLine().toCharArray();
        }

        Set<Character> visited = new HashSet<>();
        visited.add(board[0][0]);

        System.out.println(move(0, 0, visited, 1));
    }

    static int move(int curR, int curC, Set<Character> visited, int curCount) {
        int result = curCount;

        for (int i = 0; i < 4; i++) {
            int nextR = curR + dr[i];
            int nextC = curC + dc[i];

            if (nextR >= 0 && nextR < R && nextC >= 0 && nextC < C) {
                if (!visited.contains(board[nextR][nextC])) {
                    visited.add(board[nextR][nextC]);
                    result = Math.max(result, move(nextR, nextC, visited, curCount + 1));
                    visited.remove(board[nextR][nextC]);
                }
            }
        }

        return result;
    }
}