T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    len_str1 = len(str1)
    len_str2 = len(str2)

    i = 0
    j = 0

    while len_str1 > i and len_str2 > j:
        if str1[i] != str2[j]:
            j = j - i
            i = -1
        j += 1
        i += 1

    if i == len_str1:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))
