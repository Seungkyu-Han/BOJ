import sys

N, K = map(int, sys.stdin.readline().split())

candidate_weight = []
candidate_value = []

for i in range(N):
    W, V = map(int, sys.stdin.readline().split())
    candidate_weight.append(W)
    candidate_value.append(V)

result = [0 for i in range(K + 1)]

for i in range(N):
    for t in range(K, candidate_weight[i] - 1, -1):
        result[t] = max(result[t], result[t-candidate_weight[i]] + candidate_value[i])

print(max(result))