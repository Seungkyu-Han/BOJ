import sys

input_str = sorted(list(sys.stdin.readline().strip()))

start = ""
mid = ""
end = ""

chance = 0 if len(input_str) % 2 == 0 else 1

cur_char = ""

for i in input_str:
    if cur_char == "":
        cur_char = i
    else:
        if cur_char == i:
            start = start + cur_char
            end = cur_char + end
            cur_char = ""
        else:
            chance -= 1
            mid = cur_char
            cur_char = i

if cur_char != "":
    mid = cur_char

if chance >= 0:
    print(start + mid + end)
else:
    print("I'm Sorry Hansoo")