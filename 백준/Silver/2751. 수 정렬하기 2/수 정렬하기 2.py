import sys

input_numbers = list()

for _ in range(int(sys.stdin.readline())):
    input_numbers.append(int(sys.stdin.readline()))

for number in sorted(input_numbers):
    print(number)