import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
answer = []

for i in range(1,11):
    for j in list(combinations(range(10),i)):
        decrease_Number = ""
        for k in sorted(j, reverse = True):
            decrease_Number += str(k)
        answer.append(int(decrease_Number))

answer.sort()

if(n >= len(answer)):
    print(-1)
else:
    print(answer[n])