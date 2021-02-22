T = int(input())

for tc in range(1, T+1):
    str1 = list(set(input()))
    str2 = input()

    count_dict = dict(zip(str1, [0]*len(str1)))

    for each_char in str2:
        if count_dict.get(each_char, -1) == -1:
            pass
        else:
            count_dict[each_char] += 1

    answer = 0
    for i in count_dict.values():
        if answer < i:
            answer = i

    print('#{} {}'.format(tc, answer))

    