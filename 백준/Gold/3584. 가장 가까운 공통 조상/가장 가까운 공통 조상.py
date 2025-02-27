import sys

T: int = int(sys.stdin.readline())

for _ in range(T):

    N: int = int(sys.stdin.readline())

    parent_dict: dict[int, int] = {i + 1: i + 1 for i in range(N)}
    child_dict: dict[int, list[int]] = {i + 1: [] for i in range(N)}
    depth: dict[int, int] = {i + 1: 0 for i in range(N)}

    for _ in range(N - 1):
        A, B = map(int, sys.stdin.readline().split())

        parent_dict[B] = A
        child_dict[A].append(B)

    target_a, target_b = map(int, sys.stdin.readline().split())

    root_node = -1

    for i in range(1, N + 1):
        if parent_dict[i] == i:
            root_node = i
            break

    need_visit:list[int] = [root_node]

    while need_visit:
        cur_node:int = need_visit.pop()

        for next_node in child_dict[cur_node]:
            depth[next_node] = depth[cur_node] + 1
            need_visit.append(next_node)

    cur_depth:int = max(depth[target_a], depth[target_b])


    while cur_depth >= 0:

        if depth[target_a] >= cur_depth:
            target_a = parent_dict[target_a]

        if depth[target_b] >= cur_depth:
            target_b = parent_dict[target_b]

        if target_a == target_b:
            print(target_a)
            break

        cur_depth -= 1
