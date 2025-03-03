import sys

exp = list(sys.stdin.readline().rstrip())

per_stack: list[int] = []
per_set: list[list[int]] = []

for i in range(len(exp)):
    if exp[i] == '(':
        per_stack.append(i)
    elif exp[i] == ')':
        set_per = per_stack.pop()

        per_set.append([set_per, i])


per_set.sort()

start, end = 1, 2 ** len(per_set)

length = len(per_set)

result = set()

for i in range(start, end):

    avoid_set: set[int] = set()

    for j in range(length):
        if 2 ** j & i > 0:
            avoid_set.add(per_set[length - j - 1][0])
            avoid_set.add(per_set[length - j - 1][1])

    result_exp = ''

    for j in range(len(exp)):
        if j not in avoid_set:
            result_exp += exp[j]

    result.add(result_exp)

result = sorted(list(result))

for i in result:
    print(i)