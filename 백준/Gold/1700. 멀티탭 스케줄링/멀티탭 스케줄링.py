import sys
import heapq

N, K = map(int, sys.stdin.readline().split())

plugs = list(map(int, sys.stdin.readline().split()))
input_plug_set = set(plugs)
last_use = [K + 1 for _ in range(K)]
last_use_dict = {i: K + 1 for i in list(input_plug_set)}

for i in range(K - 1, -1, -1):
    cur_plug = plugs[i]

    last_use[i] = last_use_dict[cur_plug]
    last_use_dict[cur_plug] = i


cur_plugged = set()
cur_recent_use = {i: K + 1 for i in list(input_plug_set)}
result = 0

for i in range(K):
    cur_plug = plugs[i]
    cur_recent_use[cur_plug] = last_use[i]

    if cur_plug in cur_plugged:
        continue

    if len(cur_plugged) < N:
        cur_plugged.add(cur_plug)
    else:
        cur_plugged_to_list = list(cur_plugged)
        unplugged = cur_plugged_to_list[0]

        for j in range(len(cur_plugged_to_list)):
            cur_unplugged = cur_plugged_to_list[j]
            if cur_recent_use[unplugged] < cur_recent_use[cur_unplugged]:
                unplugged = cur_unplugged

        cur_plugged.remove(unplugged)
        cur_plugged.add(cur_plug)
        result += 1

print(result)