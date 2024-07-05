N = int(input())

start = 1
end = 7

index = 1

while not (start <= N <= end):
    start = end + 1
    index += 1
    end += (index * 6)

if N == 1:
    print(1)
else:
    print(index + 1)