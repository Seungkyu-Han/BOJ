import sys
import math

def is_z(num):
    if math.ceil(num) > num:
        return False
    else:
        return True

N = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

if N < 3:
    if N == 2 and nums[0] == nums[1]:
        print(nums[0])
    else:
        print('A')
else:
    
    if nums[1] != nums[0]:
        a = (nums[2] - nums[1]) / (nums[1] - nums[0])
    else:
        a = 0

    b = nums[1] - (a * nums[0])

    flag = True

    int_a = int(a)
    int_b = int(b)

    if is_z(a) and is_z(b):
        for i in range(N - 1):
            if nums[i] * int_a + int_b != nums[i + 1]:
                flag = False
                break

        if flag:
            print(nums[-1] * int_a + int_b)
        else:
            print('B')


    else:
        print('B')