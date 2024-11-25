A, B, C = map(int, input().split())


def multiply(x, y, z):
    if y == 1:
        return x % z
    elif y % 2 == 0:
        result = multiply(x, y // 2, z)
        return (result * result) % z
    else:
        result = multiply(x, y // 2, z)
        return (result * result * x) % z

print(multiply(A, B, C))