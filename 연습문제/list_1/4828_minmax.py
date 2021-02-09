initial_input = int(input())
k = 0

for each_tc in range(initial_input):
    nums = int(input())
    nums_list = list(map(int, input().split()))

    # 버블 정렬을 해보자
    for i in range(len(nums_list)-1,0,-1):
        for j in range(i):
            if nums_list[j] > nums_list[j+1]:
                nums_list[j], nums_list[j+1] = nums_list[j+1], nums_list[j]

    answer = nums_list[-1] - nums_list[0]
    k += 1

    print('#{} {}'.format(k, answer))


