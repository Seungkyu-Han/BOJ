import sys

sys.setrecursionlimit(10**6)

tree = []

while True:
    try:
        tree.append(int(sys.stdin.readline()))
    except:
        break

def suf(cur_list):

    if len(cur_list) < 1:
        return

    left, right = [], []

    target = cur_list[0]

    for node in cur_list[1:]:
        if node < target:
            left.append(node)
        else:
            right.append(node)

    if len(left) > 0:
        suf(left)
    if len(right) > 0:
        suf(right)
    print(target)


suf(tree)