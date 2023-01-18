import sys

K, N, F = map(int, sys.stdin.readline().split())

friends = [[] for i in range(N + 1)]

for i in range(F):
    a, b = map(int, sys.stdin.readline().split())
    friends[a].append(b)
    friends[b].append(a)


# 새로 들어온 친구가 들어갈 수 있는지 확인하는 함수이다.
# 리스트에 첫 번째 인덱스는 0이 있으니 제외하고 시작하자.
def is_friend(plus_friend, member_list):
    for q in member_list[1:]:
        if plus_friend not in friends[q]:
            return False
    return True


# cur_cnt는 현재 만들어진 멤버의 수, cur_list는 그 멤버의 번호이다.
def find_friends(cur_cnt, cur_list):

    # 멤버를 K명 모으면 함수를 종료한다. (재귀함수의 기저사례)
    if cur_cnt == K:
        for q in cur_list[1:]:
            print(q)
        return True

    # 순서대로 들어가기 때문에 cur_list에 있는 번호가 가장 큰 멤버는 -1의 인덱스에 있다.
    # 대신 빈 리스트에 -1을 부르면 에러가 뜨기 때문에 이 함수 호출 전에 반복문으로 0을 넣어주고 시작한다.
    for q in range(cur_list[-1] + 1, N + 1):
        if is_friend(q, cur_list):
            cur_list.append(q)
            if find_friends(cur_cnt + 1, cur_list):
                return True
            cur_list.pop()
    return False


if not find_friends(0, [0]):
    print(-1)