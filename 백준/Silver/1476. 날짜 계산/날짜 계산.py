import sys

E, S, M = map(int, sys.stdin.readline().split())

cur_year = 1

while True:
    if (cur_year - E) % 15 == 0 and (cur_year - S) % 28 == 0 and (cur_year - M) % 19 == 0:
        break
    cur_year += 1

print(cur_year)