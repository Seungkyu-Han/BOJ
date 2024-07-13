import sys

ring_dict = dict()
result = 0

for _ in range(int(sys.stdin.readline())):
    name, ring = map(str, sys.stdin.readline().split())

    if ring == "-":
        continue

    if ring in ring_dict:
        ring_dict[ring].append(name)
        if len(ring_dict[ring]) == 2:
            result += 1
        elif len(ring_dict[ring]) == 3:
            result -= 1
    else:
        ring_dict[ring] = [name]

print(result)

for ring in ring_dict.keys():
    if len(ring_dict[ring]) == 2:
        print(ring_dict[ring][0], ring_dict[ring][1])