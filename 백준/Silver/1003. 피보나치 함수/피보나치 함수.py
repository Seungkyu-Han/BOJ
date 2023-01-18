list1 = [[0, 0] for i in range(41)]

list1[0] = [1, 0]
list1[1] = [0, 1]

for i in range(39):
    zero = list1[i+1][1]
    one = sum(list1[i+1])
    list1[i+2] = [zero, one]

num = int(input())
for _ in range(num):
    n = int(input())
    print('{} {}' .format(list1[n][0], list1[n][1]))
    