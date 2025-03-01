import sys

T = int(sys.stdin.readline())


def reg(cur_str: str) -> bool:

    if len(cur_str) == 0:
        return True

    if cur_str.startswith("01"):
        return reg(cur_str[2:])

    elif cur_str.startswith("10"):
        cur_str = cur_str.removeprefix("10")
        if cur_str.startswith("0"):
            while cur_str.startswith("0"):
                cur_str = cur_str.removeprefix("0")

            if cur_str.startswith("1"):
                result = False
                while cur_str.startswith("1"):
                    cur_str = cur_str.removeprefix("1")
                    result = reg(cur_str) or result
                return result
            else:
                return False
        else:
            return False
    else:
        return False



for _ in range(T):
    pattern = sys.stdin.readline().rstrip()

    print('YES' if reg(pattern) else 'NO')
