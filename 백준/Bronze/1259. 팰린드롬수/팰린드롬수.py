import sys


def drome(word):
    for i in range(len(word)//2):
        if word[i] != word[-(i + 1)]:
            return False
    return True


while True:
    input_word = sys.stdin.readline().strip()

    if input_word == '0':
        break

    print('yes' if drome(input_word) else 'no')
