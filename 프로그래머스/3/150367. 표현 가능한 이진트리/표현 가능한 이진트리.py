def solution(numbers):
    answer = []

    for i in numbers:
        cur = find_list(i)
        if is_bin_tree(cur):
            answer.append(1)
        else:
            answer.append(0)

    return answer


def find_list(n):
    bin_list = []

    cnt = 0

    while n > 0:
        cnt += 1
        bin_list.append(n % 2)
        n //= 2

    bin_list.reverse()

    cur_length = len(bin_list)

    n = 1

    while not (2 ** (n - 1)) <= cur_length < (2 ** n):
        n += 1

    target_length = 2 ** n - 1

    bin_list = [0 for _ in range(target_length - len(bin_list))] + bin_list

    return bin_list


def is_bin_tree(bin_list):
    length = len(bin_list)


    if length == 1:
        return True

    mid = length // 2

    if bin_list[mid] == 0:
        if sum(bin_list) == 0:
            return True
        else:
            return False
    else:
        return is_bin_tree(bin_list[:mid]) and is_bin_tree(bin_list[mid + 1:])