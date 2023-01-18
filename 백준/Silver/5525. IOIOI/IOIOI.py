N = int(input())
input()
ans = input()

result = 'IO' * N + 'I'

mylen = 2 * N + 1

total = 0


for i in range(len(ans) - mylen):
    if ans[i] == 'I':
        if ans[i:i + mylen] == result:
            total += 1

print(total)