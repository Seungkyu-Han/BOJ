import java.lang.Math;
import java.util.*;

class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        int answer = 0;
        int end = Arrays.stream(diffs).max().getAsInt();
        int start = 1;
        
        while (start <= end){
            int mid = (start + end) / 2;
            
            boolean cur = get_time(diffs, times, mid, limit);
            
            if (cur){
                end = mid - 1;
            }
            else{
                start = mid + 1;       
            }
        }
        
        return start;
    }
    
    private boolean get_time(int[] diffs, int[] times, int level, long limit){
        long spent_time = 0;
        
        int length = diffs.length;
        
        for (int i = 0; i < length; i++){
            
            if(level >= diffs[i]){
                spent_time += times[i];
            }
            else{
                int rep_count = diffs[i] - level;
                
                int solved_time = (times[i] + times[i - 1]) * rep_count;
                solved_time += times[i];
                
                spent_time += solved_time;
            }
            
        }
        
        return spent_time <= limit;
    }
}