N, K = map(int, input().split())

def count_bit1(num):

    result = 0

    while num > 0:
        result += (num % 2)
        num //= 2

    return result


res = 0

while True:
    
    if res >= 10 ** 7:
        print(-1)
        break

    if count_bit1(res + N) <= K:
        print(res)
        break

    else:
        res += 1
