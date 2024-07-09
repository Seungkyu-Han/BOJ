def solution(array):
    answer = 0
    arr = [0 for _ in range(1000)]
    for number in array:
        arr[number] += 1
    first, second = [0, 0], [0, 0]
    for i in range(1000):
        if arr[i] >= first[0]:
            second = first
            first = [arr[i], i]
        elif arr[i] >= second[0]:
            second = [arr[i], i]
    return first[1] if first[0] != second[0] else -1