def ccw(a, b, c):
    """Counter Clockwise 함수: 점 a, b, c의 회전 방향을 계산"""
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def is_intersect(L1, L2):
    """두 선분 L1, L2가 교차하는지 확인"""
    p1, p2 = (L1[0], L1[1]), (L1[2], L1[3])
    p3, p4 = (L2[0], L2[1]), (L2[2], L2[3])

    # ccw 계산
    ccw1 = ccw(p1, p2, p3) * ccw(p1, p2, p4)
    ccw2 = ccw(p3, p4, p1) * ccw(p3, p4, p2)

    # ccw1과 ccw2로 교차 여부 판단
    if ccw1 <= 0 and ccw2 <= 0:
        # 선분 범위 내에서 실제로 교차하는지 확인
        if min(p1[0], p2[0]) <= max(p3[0], p4[0]) and min(p3[0], p4[0]) <= max(p1[0], p2[0]) and \
           min(p1[1], p2[1]) <= max(p3[1], p4[1]) and min(p3[1], p4[1]) <= max(p1[1], p2[1]):
            return True
    return False


# 입력
import sys
L1 = list(map(int, sys.stdin.readline().split()))
L2 = list(map(int, sys.stdin.readline().split()))

# 결과 출력
if is_intersect(L1, L2):
    print(1)
else:
    print(0)
