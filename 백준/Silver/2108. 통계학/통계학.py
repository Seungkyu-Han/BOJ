import sys
from collections import Counter

input_numbers = []

for _ in range(int(sys.stdin.readline())):
    input_numbers.append(int(sys.stdin.readline()))

input_numbers.sort()

print(round((sum(input_numbers))/(len(input_numbers))))
print(input_numbers[len(input_numbers) // 2])
if len(input_numbers) > 1:
    counter = Counter(input_numbers).most_common(2)
    print(counter[0][0] if counter[0][1] != counter[1][1] else counter[1][0])
else:
    print(input_numbers[0])
print(input_numbers[-1] - input_numbers[0])

