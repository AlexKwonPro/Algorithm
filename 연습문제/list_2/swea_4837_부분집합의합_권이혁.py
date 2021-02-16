T = int(input())

for tc in range(1, T+1):
    N, K = list(map(int, input().split())) # N은 원소 갯수, K는 원소의 합
    numbers_list = [x for x in range(1,13)]
    answer = 0

    for i in range(1<<12):
        count = 0
        each_arr = []
        for j in range(12):
            if i & (1<<j):
                count += numbers_list[j]
                each_arr.append(numbers_list[j])

        if K == count and N == len(each_arr):
            answer += 1

    print('#{} {}'.format(tc, answer))




