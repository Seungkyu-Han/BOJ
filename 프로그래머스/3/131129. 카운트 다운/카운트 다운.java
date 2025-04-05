import java.util.*;
import java.lang.Math;

class Solution {
    public int[] solution(int target) {
        
        int[][] dp = new int[target + 1][];
        for (int i = 0; i <= target; i++) {
           dp[i] = new int[]{1000000, 1000000};
        }
        
        Queue<Integer> count_heap = new LinkedList<>();
        count_heap.add(0);
        Queue<Integer> hit_heap = new LinkedList<>();
        hit_heap.add(0);
        Queue<Integer> score_heap = new LinkedList<>();
        score_heap.add(target);
        
        while (count_heap.size() > 0){
            int cur_count = count_heap.poll();
            int cur_hit = hit_heap.poll();
            int cur_score = score_heap.poll();
            
            int next_count = cur_count + 1;
            
            for(int i = 1; i <= 20; i++){
                for(int ii = 1; ii <= 3; ii++){
                    int next_hit = (ii == 1) ? cur_hit + 1 : cur_hit;
                    int next_score = cur_score - (i * ii);
                    
                    if(next_score < 0)
                        continue;
                    
                    if (dp[next_score][0] > next_count || 
                        (dp[next_score][0] == next_count && dp[next_score][1] < next_hit)){
                        dp[next_score][0] = next_count;
                        dp[next_score][1] = next_hit;
                        
                        count_heap.add(next_count);
                        hit_heap.add(next_hit);
                        score_heap.add(next_score);
                    }
                }
            }
            
            int next_hit = cur_hit + 1;
            int next_score = cur_score - 50;
                    
            if(next_score < 0)
                continue;

            if(dp[next_score][0] > next_count ||
              (dp[next_score][0] == next_count || 
                (dp[next_score][0] == next_count && dp[next_score][1] < next_hit))){
                dp[next_score][0] = next_count;
                dp[next_score][1] = next_hit;

                count_heap.add(next_count);
                hit_heap.add(next_hit);
                score_heap.add(next_score);
            }
        }
        
        
        return dp[0];
    }
}