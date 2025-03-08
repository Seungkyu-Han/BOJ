import sys
import heapq

ord_a = ord('a')
ord_z = ord('z')
ord_A = ord('A')
ord_Z = ord('Z')


def to_dist(ch: chr) -> int:

    if ch == '0':
        return -1

    to_ord = ord(ch)

    if ord_a <= to_ord <= ord_z:
        return to_ord - ord_a + 1
    else:
        return to_ord - ord_A + 27


N = int(sys.stdin.readline())

cables: list[list[int]] = [[0 for _ in range(N)] for _ in range(N)]
cable_heap: list[list[int]] = []


for i in range(N):

    cur_cables = list(sys.stdin.readline().rstrip())

    for j in range(N):
        distance = to_dist(cur_cables[j])
        cables[i][j] = distance

        if distance != -1:
            heapq.heappush(cable_heap, [distance, i, j])


def find(cur_node: int, parent_dict: dict[int, int]) -> int:
    if cur_node != parent_dict[cur_node]:
        parent_dict[cur_node] = find(parent_dict[cur_node], parent_dict)
    return parent_dict[cur_node]

def union(node1: int, node2: int, parent_dict: dict[int, int], rank_dict: dict[int, int]):
    root1 = find(node1, parent_dict)
    root2 = find(node2, parent_dict)

    if rank_dict[root1] > rank_dict[root2]:
        parent_dict[root2] = root1
    else:
        if rank_dict[root1] == rank_dict[root2]:
            rank_dict[root2] += 1
        parent_dict[root1] = root2


to_donation: int = 0
parent: dict[int, int] = {i: i for i in range(N)}
rank: dict[int, int] = {i: 0 for i in range(N)}

while cable_heap:

    cur_dist, cur_node1, cur_node2 = heapq.heappop(cable_heap)

    if find(cur_node1, parent) != find(cur_node2, parent):
        union(node1 = cur_node1, node2 = cur_node2, parent_dict = parent, rank_dict = rank)
    else:
        to_donation += cur_dist


is_complete = True

for i in range(N):
    if find(i, parent) != find(0, parent):
        is_complete = False
        break

if is_complete:
    print(to_donation)
else:
    print(-1)