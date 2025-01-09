import sys

sys.setrecursionlimit(10**6)

G = int(sys.stdin.readline())

P = int(sys.stdin.readline())

gate = [i for i in range(G + 1)]

airplanes = [int(sys.stdin.readline()) for _ in range(P)]

def find(cur_node):
    if gate[cur_node] != cur_node:
        gate[cur_node] = find(gate[cur_node])
    return gate[cur_node]

def find_gate(cur_airplane):
    node = find(cur_airplane)

    if node > 0:
        gate[node] = node - 1
        return True
    else:
        return False

result = 0

for airplane in airplanes:

    if find_gate(airplane):
        result += 1
    else:
        break

print(result)