from itertools import permutations

def check(s1, s2):
    if len(s1) != len(s2):
        return False
    for a, b in zip(s1, s2):
        if a == '*':
            continue
        if a != b:
            return False
    return True

def solution(user_id, banned_id):
    result_set = set()

    for perm in permutations(user_id, len(banned_id)):
        if all(check(b, u) for b, u in zip(banned_id, perm)):
            result_set.add(tuple(sorted(perm)))  # 중복 방지용 정렬

    return len(result_set)
