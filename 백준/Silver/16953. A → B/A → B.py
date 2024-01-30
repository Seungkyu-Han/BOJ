import sys

A, B = map(int, sys.stdin.readline().split())

greedy = set()
greedy.add(A)

result = 1

while B not in greedy and greedy:

    current_greedy = set()

    while greedy:
        element = greedy.pop()
        if element * 2 <= 10 ** 9:
            current_greedy.add(element * 2)
        if element * 10 + 1 <= 10 ** 9:
            current_greedy.add(element * 10 + 1)

    result += 1
    greedy = current_greedy


print(result if greedy else -1)