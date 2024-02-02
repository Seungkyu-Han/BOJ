import sys

word = [0 for i in range(ord('Z') - ord('A') + 1)]

for i in range(int(sys.stdin.readline().strip())):

    input_word = str(sys.stdin.readline().strip())

    cur_index = 1

    while input_word:
        word[ord(input_word[-1]) - ord('A')] += cur_index
        cur_index *= 10
        input_word = input_word[:-1]

word.sort(reverse=True)

result = 0

for i in range(10):
    result += (word[i] * (9-i))

print(result)