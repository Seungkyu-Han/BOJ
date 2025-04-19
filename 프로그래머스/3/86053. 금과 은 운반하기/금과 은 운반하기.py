def solution(a, b, g, s, w, t):
    def check(time):
        total_sum = 0
        total_a = 0
        total_b = 0
        for i in range(len(g)):
            round_trip = 2 * t[i]
            count = time // round_trip
            if time % round_trip >= t[i]:  # 편도 갈 수 있는 시간 남으면 +1
                count += 1
            max_weight = count * w[i]
            total_sum += min(max_weight, g[i] + s[i])
            total_a += min(max_weight, g[i])
            total_b += min(max_weight, s[i])
            if total_sum >= a + b and total_a >= a and total_b >= b:
                return True
        if total_sum < a + b:
            return False
        if total_a < a:
            return False
        if total_b < b:
            return False
        return True

    start = 0
    end = 4 * (10 ** 14)
    while start < end:
        mid = (start + end) // 2
        if check(mid):
            end = mid
        else:
            start = mid + 1
    return start
