import sys

num = int(sys.stdin.readline())

list1 = []

for i in range(num):
    ans = sys.stdin.readline().split()
    if ans[0] == 'push':
        list1.append(int(ans[1]))
    elif ans[0] == 'pop':
        if len(list1) == 0:
            print(-1)
        else:
            print(list1.pop(0))
    elif ans[0] == 'size':
        print(len(list1))
    elif ans[0] == 'empty':
        print(1 if len(list1) == 0 else 0)
    elif ans[0] == 'front':
        print(-1 if len(list1) == 0 else list1[0])
    elif ans[0] == 'back':
        print(-1 if len(list1) == 0 else list1[len(list1) - 1])

