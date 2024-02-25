import sys

input_string = sys.stdin.readline().strip()

string_set = set()

for i in range(1, len(input_string)):
    for t in range(0, len(input_string) + 1):
        string_set.add(input_string[t:t+i])

print(len(string_set))