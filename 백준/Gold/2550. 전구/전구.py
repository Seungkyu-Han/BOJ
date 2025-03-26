import sys
import bisect

dp = []
sequence = []

N = int(sys.stdin.readline())
switches = list(map(int, sys.stdin.readline().split()))
bulbs = list(map(int, sys.stdin.readline().split()))

# 전구 번호 -> 인덱스 매핑
bulb_dict = {bulbs[i]: i + 1 for i in range(N)}

# 추적용 배열 초기화
position = [-1] * N

for i in range(N):
    cur_switch = switches[i]
    bulb_position = bulb_dict[cur_switch]

    if not dp or dp[-1] < bulb_position:
        if dp:
            position[i] = sequence[-1]  # 이전 인덱스 저장
        dp.append(bulb_position)
        sequence.append(i)
    else:
        index = bisect.bisect_left(dp, bulb_position)
        dp[index] = bulb_position
        if index > 0:
            position[i] = sequence[index - 1]  # 이전 인덱스 저장
        sequence[index] = i

# LIS 개수 출력
print(len(dp))

# LIS 역추적
result = []
idx = sequence[len(dp) - 1]
while idx != -1:
    result.append(switches[idx])
    idx = position[idx]

# 정렬 후 출력
result.sort()
print(*result)
