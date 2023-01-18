num = int(input())

km = list(map(int, input().split()))
oil = list(map(int, input().split()))

total = 0
ptr = 0

while ptr < num - 1:
    length = km[ptr]
    go = 1
    while oil[ptr] < oil[ptr + go] and ptr + go < num:
        length += km[ptr + go]
        go += 1
    total += (length * oil[ptr])
    ptr += go

print(total)