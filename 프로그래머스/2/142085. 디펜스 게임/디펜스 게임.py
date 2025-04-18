import heapq

def solution(n, k, enemy):
    answer = 0
    cur_n = n
    heap = []

    for i in range(len(enemy)):
        heapq.heappush(heap, -enemy[i])
        cur_n -= enemy[i]

        if cur_n < 0:
            if k == 0:
                break
            # 가장 많이 소비된 병력을 무적권으로 교체
            max_enemy = -heapq.heappop(heap)
            cur_n += max_enemy
            k -= 1
        answer = i + 1

    return answer
