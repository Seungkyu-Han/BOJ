import java.util.*;

class Solution {
    
    private final int[][] fatigue = {
        {1, 1, 1},   // 다이아 곡괭이
        {5, 1, 1},   // 철 곡괭이
        {25, 5, 1}   // 돌 곡괭이
    };

    public int solution(int[] picks, String[] minerals) {
        int answer = 0;
        
        // 최대 곡괭이 개수만큼 광물 캐기
        int maxMine = Math.min(minerals.length, (picks[0] + picks[1] + picks[2]) * 5);

        // 5개씩 그룹으로 나누기
        List<int[]> mineralGroups = new ArrayList<>();
        for (int i = 0; i < maxMine; i += 5) {
            int[] group = new int[3]; // diamond, iron, stone 개수
            for (int j = i; j < Math.min(i + 5, maxMine); j++) {
                if (minerals[j].equals("diamond")) group[0]++;
                else if (minerals[j].equals("iron")) group[1]++;
                else group[2]++;
            }
            mineralGroups.add(group);
        }

        // 다이아 > 철 > 돌 많은 순으로 정렬
        mineralGroups.sort((a, b) -> (b[0] * 25 + b[1] * 5 + b[2]) - (a[0] * 25 + a[1] * 5 + a[2]));

        // 최적의 곡괭이 배정
        for (int[] group : mineralGroups) {
            int pickType = -1;

            if (picks[0] > 0) { // 다이아 곡괭이 사용
                pickType = 0;
                picks[0]--;
            } else if (picks[1] > 0) { // 철 곡괭이 사용
                pickType = 1;
                picks[1]--;
            } else if (picks[2] > 0) { // 돌 곡괭이 사용
                pickType = 2;
                picks[2]--;
            } else {
                break; // 곡괭이가 없으면 종료
            }

            // 피로도 계산
            answer += group[0] * fatigue[pickType][0]; // 다이아몬드 개수
            answer += group[1] * fatigue[pickType][1]; // 철 개수
            answer += group[2] * fatigue[pickType][2]; // 돌 개수
        }

        return answer;
    }
}
