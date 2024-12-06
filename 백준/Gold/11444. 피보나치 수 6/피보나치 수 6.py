import sys

sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline())

fibonacci_array = {0: 0, 1: 1, 2: 1}


def fibonacci(cur_n):
    if cur_n <= 2:
        return fibonacci_array[cur_n]

    if cur_n % 2 == 0:
        next_index = cur_n // 2
        if next_index not in fibonacci_array:
            fibonacci_array[next_index] = fibonacci(next_index)

        if next_index - 1 not in fibonacci_array:
            fibonacci_array[next_index - 1] = fibonacci(next_index - 1)
        return (fibonacci_array[next_index] * (2 * fibonacci_array[next_index - 1] + fibonacci_array[next_index])) % 1_000_000_007
    else:
        next_index = cur_n // 2
        if next_index not in fibonacci_array:
            fibonacci_array[next_index] = fibonacci(next_index)

        if next_index + 1 not in fibonacci_array:
            fibonacci_array[next_index + 1] = fibonacci(next_index + 1)

        return (fibonacci_array[next_index] ** 2 + fibonacci_array[next_index + 1] ** 2) % 1_000_000_007


print(fibonacci(n))