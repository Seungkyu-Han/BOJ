result = [True for i in range(1, 10001)]

def d(n):
    d_result = n

    while n > 9:
        d_result += (n % 10)
        n //= 10

    return d_result + n


for i in range(1, 10000):
    if result[i]:
        print(i)
        num = i
        while num < 10000:
            num = d(num)
            if num < 10000:
                result[num] = False
