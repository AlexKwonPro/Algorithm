m = 0
for tc in range(10):
    dump_num = int(input())
    heights_list = list(map(int, input().split()))

        #  할수있는 덤프 횟수만큼 포문을 돌리면서?
        #  앞뒤로 비교하는 식으로 한번 순회하면서 최소, 최댓값 적어주고?
        #  최대 - 최소값 구하면 될듯.

    for i in range(dump_num):
        # heights_list 가 바뀌어야 하는데?
        max_height = heights_list[0]
        max_idx = 0
        min_height = heights_list[0]
        min_idx = 0

        for idx, each_column in enumerate(heights_list):
            if max_height < each_column:
                max_height = each_column
                max_idx = idx

            if min_height > each_column:
                min_height = each_column
                min_idx = idx
        # 이녀석이 if랑 동일선에 있으면 조짐.
        heights_list[max_idx] -= 1
        heights_list[min_idx] += 1

    max_height = heights_list[0]
    min_height = heights_list[0]

    for j in heights_list:  # 덤핑 n회 이후의 height_list

        if max_height < j:
            max_height = j

        if min_height > j:
            min_height = j

    answer = max_height - min_height
    m += 1
    print('#{} {}'.format(m, answer))
