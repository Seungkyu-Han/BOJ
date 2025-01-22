import sys


def find(parent_dict_param, node):
    if parent_dict_param[node] != node:
        parent_dict_param[node] = find(parent_dict, parent_dict_param[node])
    return parent_dict_param[node]

def union(parent_dict_param, rank_dict_param, count_dict_param, node1, node2):
    root1 = find(parent_dict_param, node1)
    root2 = find(parent_dict_param, node2)

    if root1 != root2:

        if rank_dict_param[root1] > rank_dict_param[root2]:
            parent_dict_param[root2] = root1
            count_dict_param[root1] += count_dict_param[root2]
        else:
            parent_dict_param[root1] = root2
            count_dict_param[root2] += count_dict_param[root1]
            if rank_dict_param[root1] == rank_dict_param[root2]:
                rank_dict_param[root2] += 1



def count_relation(parent_dict_param, node):
    count = 0

    for name in parent_dict_param.keys():
        if find(parent_dict_param, name) == node:
            count += 1
    return count


for _ in range(int(sys.stdin.readline())):

    F = int(sys.stdin.readline())

    parent_dict = dict()
    rank_dict = dict()
    count_dict = dict()

    for _ in range(F):
        user1, user2 = map(str, sys.stdin.readline().split())

        if user1 not in parent_dict:
            parent_dict[user1] = user1
            rank_dict[user1] = 0
            count_dict[user1] = 1

        if user2 not in parent_dict:
            parent_dict[user2] = user2
            rank_dict[user2] = 0
            count_dict[user2] = 1

        union(parent_dict, rank_dict, count_dict, user1, user2)

        print(count_dict[find(parent_dict, user1)])
