import sys

S = list(sys.stdin.readline().rstrip())

a_ord = ord('a')
z_ord = ord('z')

total_length = len(S)

alpha_dict = dict()

for s in S:
    if s in alpha_dict:
        alpha_dict[s] += 1
    else:
        alpha_dict[s] = 1
def back_tracking(last_word, cur_dict, cur_length):

    result = 0

    if cur_length == 0:
        return 1

    for cur_chr in cur_dict.keys():

        if cur_dict[cur_chr] > 0 and last_word != cur_chr:
            cur_dict[cur_chr] -= 1
            result += back_tracking(cur_chr, cur_dict, cur_length - 1)
            cur_dict[cur_chr] += 1

    return result

print(back_tracking('A', alpha_dict, total_length))
