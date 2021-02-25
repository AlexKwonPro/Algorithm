T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers_list = list(map(int, input().split()))

    for i in range(N-1,0,-1):
        for j in range(i):
            if numbers_list[j] > numbers_list[j+1]:
                numbers_list[j], numbers_list[j+1] = numbers_list[j+1], numbers_list[j]

    # print('#{}'.format(tc), end= " ")
    # print(*numbers_list)

    print('#{} {}'.format(tc, ' '.join(map(str,numbers_list))))

    