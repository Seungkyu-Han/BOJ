import sys

def is_palin(cur_string):
    if len(cur_string) < 2:
        return 0

    start, end = 0, len(cur_string) - 1

    while start < end:
        if cur_string[start] != cur_string[end]:
            # 한 문자 제거 후 재검사
            skip_left = cur_string[start + 1:end + 1]
            skip_right = cur_string[start:end]
            if skip_left == skip_left[::-1] or skip_right == skip_right[::-1]:
                return 1
            else:
                return 2
        start += 1
        end -= 1
    return 0


# 안전한 입력 처리
try:
    T = sys.stdin.readline().strip()
    T = int(T) if T.isdigit() else 0

    for _ in range(T):
        input_string = sys.stdin.readline().strip()
        if input_string:  # 빈 문자열 처리
            print(is_palin(input_string))
except Exception as e:
    print(f"Error: {e}")
