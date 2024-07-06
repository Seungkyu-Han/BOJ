import sys
import bisect

Q = int(sys.stdin.readline())
book_list = []


for _ in range(Q):
    query = list(map(str, sys.stdin.readline().split()))

    if query[0] == '1':
        price = int(query[1])
        bisect.insort_left(book_list, price)

    elif query[0] == '2':
        price = int(query[1])
        index = bisect.bisect_left(book_list, price)
        if 0 <= index < len(book_list) and book_list[index] == price:
            del book_list[index]
    else:
        result = 0
        cur_price = 0
        i = 0
        while i < len(book_list):
            if cur_price == 0:
                cur_price = book_list[i]
                result += 1
            else:
                next_price = cur_price * 2
                i = bisect.bisect_left(book_list, next_price, i)
                if i < len(book_list):
                    cur_price = book_list[i]
                    result += 1
                else:
                    break
        print(result)
