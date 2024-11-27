import sys

N = int(sys.stdin.readline())

tree = {chr(ord('A') + i): ['.', '.'] for i in range(N)}

for _ in range(N):
    root, left, right = map(str, sys.stdin.readline().split())
    tree[root] = [left, right]



def pre(cur_node):

    cur_left, cur_right = tree[cur_node]

    print(cur_node, end='')

    if cur_left != ".":
        pre(cur_left)

    if cur_right != ".":
        pre(cur_right)


def mid(cur_node):

    cur_left, cur_right = tree[cur_node]

    if cur_left != ".":
        mid(cur_left)

    print(cur_node, end='')

    if cur_right != ".":
        mid(cur_right)


def suf(cur_node):

    cur_left, cur_right = tree[cur_node]

    if cur_left != ".":
        suf(cur_left)

    if cur_right != ".":
        suf(cur_right)

    print(cur_node, end='')

pre('A')
print()

mid('A')
print()

suf('A')