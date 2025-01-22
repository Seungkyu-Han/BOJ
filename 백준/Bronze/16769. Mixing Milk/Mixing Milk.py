import sys

c1, m1 = map(int, sys.stdin.readline().split())
c2, m2 = map(int, sys.stdin.readline().split())
c3, m3 = map(int, sys.stdin.readline().split())

bucket = [c1, c2, c3]
milk = [m1, m2, m3]

for i in range(100):
    start = i % 3
    end = (i + 1) % 3

    moved_milk = min(bucket[end] - milk[end], milk[start])
    remained_milk = milk[start] - moved_milk

    milk[end] += moved_milk
    milk[start] = remained_milk

for i in milk:
    print(i)