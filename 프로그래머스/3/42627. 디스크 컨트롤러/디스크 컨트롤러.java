import java.util.*;
import java.lang.Math;

class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        Arrays.sort(jobs, Comparator.<int[]>comparingInt(o -> o[0])
                   .thenComparingInt(o -> o[1]));
        
        PriorityQueue<ArrayList<Integer>> q = new PriorityQueue<>(
            Comparator.<ArrayList<Integer>>comparingInt(o -> o.get(0))
                .thenComparingInt(o -> o.get(1))
        );
        
        int length = jobs.length;
        int index = 0;
        int cur_time = 0;
        
        while (index < length){
            if(q.size() == 0){
                int start_time = jobs[index][0];
                int spent_time = jobs[index][1];
                answer += spent_time;
                cur_time = Math.max(start_time, cur_time) + spent_time;
                index ++;
            }
            else{
                ArrayList<Integer> cur_job = q.poll();
                int start_time = cur_job.get(1);
                int spent_time = cur_job.get(0);
                
                cur_time += spent_time;
                answer += (cur_time - start_time);
            }
            while(index < length && cur_time >= jobs[index][0]){
                ArrayList<Integer> add_job = new ArrayList<>();
                add_job.add(jobs[index][1]);
                add_job.add(jobs[index][0]);
                q.add(add_job);
                index++;
            }
        }
        System.out.printf("%d %d\n\n", cur_time, answer);
        while (q.size() > 0){
            ArrayList<Integer> cur_job = q.poll();
            int start_time = cur_job.get(1);
            int spent_time = cur_job.get(0);

            cur_time += spent_time;
            answer += (cur_time - start_time);
            
            System.out.printf("%d %d\n", start_time, spent_time);
            System.out.printf("%d %d\n\n", cur_time, answer);
        }
        
        
        return answer / length;
    }
}