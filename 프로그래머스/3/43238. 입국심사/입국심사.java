import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        int max_time = Arrays.stream(times).max().getAsInt();
        long answer = 0;
        long start = 0, end = (long)max_time * n;
        
        while(start <= end){
            long mid = (start + end) / 2L;
            long cur_count = user_count(times, mid);
            if(cur_count >= n){
                end = mid - 1;
            }
            else{
                start = mid + 1;
            }
        }
        
        return start;
    }
    
    private long user_count(int[] times, long target){
        long result = 0;
        for(int i = 0; i < times.length; i++){
            result += (target / times[i]);
        }
        return result;
    }
}