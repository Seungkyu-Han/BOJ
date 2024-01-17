import sys

N = int(sys.stdin.readline())

end_zero = 0
end_one = 1

for i in range(N-1):
    end_zero, end_one = end_zero + end_one, end_zero

print(end_zero + end_one)