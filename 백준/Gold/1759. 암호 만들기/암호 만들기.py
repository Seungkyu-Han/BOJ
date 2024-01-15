import sys

L, C = map(int, sys.stdin.readline().split())

candidate = sorted(list(map(str, sys.stdin.readline().split())))

important = {'a', 'e', 'i', 'o', 'u'}


def make_key(cur_candidate, index):

    if index == C:
        value = len(set(cur_candidate).intersection(important))
        if len(cur_candidate) == L and value >= 1 and (L - value) >= 2:
            for i in cur_candidate:
                print(i, end='')
            print()
            return

    else:
        make_key(cur_candidate + [candidate[index]], index + 1)
        make_key(cur_candidate, index + 1)


make_key([], 0)