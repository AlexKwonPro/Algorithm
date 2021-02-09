T = int(input())
m = 0

for tc in range(T):
    integer_info = list(map(int, (input().split())))
    received_nums = list(map(int, (input().split())))
    integer_num = integer_info[0]
    interval = integer_info[1]

    all_sums_list = [] # 구간합들을 받아줄 빈 리스트 생성.

    # 예를들면 숫자들이 5개인데 3개짜리 구간을 설정했다고 하면 (5-3)  2 + 1 번만큼 연속한 다른구간이 나온다.
    for i in range(integer_num - interval + 1):
        interval_list = received_nums[i:i+interval] # 슬라이싱 할때 이렇게.
        count = 0
        for j in interval_list:
            count += j

        all_sums_list.append(count)

    # 여기까지 하면 all_sums_list 에는 구간합들이 요소로서 들어가 있을 것이므로 이걸 버블정렬 하고
    # -1 인덱스인 최댓값 - 0인덱스인 최솟값을 빼주면 완성!

    for x in range(len(all_sums_list)-1, 0, -1):
        for y in range(x):
            if all_sums_list[y] > all_sums_list[y+1]:
                all_sums_list[y], all_sums_list[y+1] = all_sums_list[y+1], all_sums_list[y]

    answer = all_sums_list[-1] - all_sums_list[0]

    m += 1

    print('#{} {}'.format(m, answer))
