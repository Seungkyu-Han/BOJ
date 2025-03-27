import sys

N, d, k, c = map(int, sys.stdin.readline().split())

sushis = []

for _ in range(N):
    sushi = int(sys.stdin.readline())

    sushis.append(sushi)


cur_sushis = {i: 0 for i in range(1, d + 1)}
sushi_set = set()
result = 0

for i in range(k):
    cur_sushi = sushis[i]
    cur_sushis[sushis[i]] += 1
    sushi_set.add(cur_sushi)

for i in range(k, N):
    del_sushi = sushis[i - k]
    add_sushi = sushis[i]

    cur_sushis[del_sushi] -= 1
    
    if cur_sushis[del_sushi] == 0:
        sushi_set.remove(del_sushi)

    cur_sushis[add_sushi] += 1
    sushi_set.add(add_sushi)

    if c in sushi_set:
        result = max(result, len(sushi_set))
    else:
        result = max(result, len(sushi_set) + 1)

for i in range(k):
    del_sushi = sushis[i - k + N]
    add_sushi = sushis[i]

    cur_sushis[del_sushi] -= 1
    
    if cur_sushis[del_sushi] == 0:
        sushi_set.remove(del_sushi)

    cur_sushis[add_sushi] += 1
    sushi_set.add(add_sushi)

    if c in sushi_set:
        result = max(result, len(sushi_set))
    else:
        result = max(result, len(sushi_set) + 1)

print(result)
