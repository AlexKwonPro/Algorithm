test_num = int(input())

for tc in range(test_num):
    column_num = int(input())
    columns_list = list(map(int, input().split()))

    initial_advantage = column_num  # 노란색의 경우 최대낙차는 컬럼갯수 - 1
    candidate_list = []

    for i in range(0, len(columns_list)-1): # 첫번째 기둥부터 끝에서 1번째 기둥.
        count = 0
        initial_advantage -= 1

        for j in range(i+1, len(columns_list)):
            if columns_list[j] >= columns_list[i]:
                count += 1

        candidate_list.append(initial_advantage - count)

        answer = 0

    for x in candidate_list:
        if x > answer:
            answer = x

    print(answer)



# 인풋 받는거
# 3
# 9
# 7 4 2 0 0 6 0 7 0
# 9
# 7 4 2 0 0 6 7 7 0
# 20
# 52 56 38 77 43 31 11 87 68 64 88 76 56 59 46 57 75 85 65 53