import java.util.*;

class Solution {
    public int[] solution(String[] gems) {
        int[] answer = {0, gems.length - 1};
        
        Map<String, Integer> gem_count = new HashMap<>();
        
        for(String gem: gems)
            gem_count.putIfAbsent(gem, 0);
        
        int total_type = gem_count.size();
        
        int start = 0, end = 0;
        int cur_type = 1;
        gem_count.replace(gems[0], 1);
        
        while (end < gems.length){
            
            if (cur_type == total_type){
                if (answer[1] - answer[0] > end - start){
                    answer[0] = start;
                    answer[1] = end;
                }
                String cur_gem = gems[start];
                gem_count.replace(cur_gem, gem_count.get(cur_gem) - 1);
                if (gem_count.get(cur_gem) == 0)
                    cur_type --;
                start ++;
            }
            else{
                if (end + 1 < gems.length){
                    String cur_gem = gems[++end];
                    gem_count.replace(cur_gem, gem_count.get(cur_gem) + 1);
                    if (gem_count.get(cur_gem) == 1)
                        cur_type ++;
                }
                else
                    break;
            }
        }
        
        answer[0]++;
        answer[1]++;
        
        return answer;
    }
}