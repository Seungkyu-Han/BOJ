import sys

judge = []

for i in range(int(sys.stdin.readline())):
    age, name = map(str, sys.stdin.readline().split())
    judge.append([int(age), i, name])

for age, i, name in list(sorted(judge)):
    print(f'{age} {name}')