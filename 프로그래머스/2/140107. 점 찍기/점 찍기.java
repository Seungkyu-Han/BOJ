import java.lang.Math;

class Solution {
    public long solution(int k, int d) {
        long answer = 0;
        long D = (long) d; // 미리 long으로 바꿔줌

        for (long i = 0; i <= D; i += k) {
            long xSquared = i * i;
            long maxYSquared = D * D - xSquared;
            long maxY = (long) Math.sqrt(maxYSquared);
            answer += (maxY / k) + 1;
        }

        return answer;
    }
}
