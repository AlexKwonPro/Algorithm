T = int(input())

for tc in range(1, T+1):
    N = int(input())  # N by N
    num_map = [list(map(int, input().split())) for _ in range(N)]

    def clockwise_90_rotate(two_dimentional_matrix):
        rotated_list = []

        for j in range(N):
            pendency_list = []
            for i in range(N-1,-1,-1):
                pendency_list.append(two_dimentional_matrix[i][j])
            rotated_list.append(pendency_list)

        return rotated_list

    rotation_90 = clockwise_90_rotate(num_map)
    rotation_180 = clockwise_90_rotate(rotation_90)
    rotation_270 = clockwise_90_rotate(rotation_180)

    print('#{}'.format(tc))

    for j in range(N):
        answer = ''.join(map(str,rotation_90[j])) + ' ' + ''.join(map(str, rotation_180[j])) + ' ' + ''.join(map(str, rotation_270[j]))
        print(answer)

    # print('#{}'.format(tc))   ## 확인용
    # for m in range(N):
    #     print(rotation_90[m])
    # print('____________________')
    #
    # for p in range(N):
    #     print(rotation_180[p])
    # print('____________________')
    #
    # for q in range(N):
    #     print(rotation_270[q])
    # print('____________________')





