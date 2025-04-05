import java.util.*;

class Solution {
    public int[] solution(int target) {
        int[][] dp = new int[target + 1][2];
        for (int i = 0; i <= target; i++) {
            dp[i][0] = Integer.MAX_VALUE; // 최소 다트 수
            dp[i][1] = Integer.MIN_VALUE; // 최대 싱글/불
        }

        dp[target][0] = 0;
        dp[target][1] = 0;

        Queue<Integer> queue = new LinkedList<>();
        queue.add(target);

        while (!queue.isEmpty()) {
            int score = queue.poll();
            int dartCount = dp[score][0];
            int hitCount = dp[score][1];

            // 1~20, 곱 1~3
            for (int i = 1; i <= 20; i++) {
                for (int mul = 1; mul <= 3; mul++) {
                    int nextScore = score - i * mul;
                    if (nextScore < 0) continue;

                    int nextDart = dartCount + 1;
                    int nextHit = hitCount + (mul == 1 ? 1 : 0);

                    if (dp[nextScore][0] > nextDart || 
                        (dp[nextScore][0] == nextDart && dp[nextScore][1] < nextHit)) {
                        dp[nextScore][0] = nextDart;
                        dp[nextScore][1] = nextHit;
                        queue.add(nextScore);
                    }
                }
            }

            // bull (50점)
            int nextScore = score - 50;
            if (nextScore >= 0) {
                int nextDart = dartCount + 1;
                int nextHit = hitCount + 1;

                if (dp[nextScore][0] > nextDart || 
                    (dp[nextScore][0] == nextDart && dp[nextScore][1] < nextHit)) {
                    dp[nextScore][0] = nextDart;
                    dp[nextScore][1] = nextHit;
                    queue.add(nextScore);
                }
            }
        }

        return dp[0];
    }
}
