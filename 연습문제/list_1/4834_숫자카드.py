T = int(input())
m = 0
for tc in range(T):
    card_num = int(input())
    card_deck = list(map(int,input()))

    count_list = [0]*(9+1)

    for i in card_deck:
        count_list[i] += 1

    # print(count_list)
    # 여기까지 하면 count_list 가 숫자카드의 숫자에 해당하는 인덱스에 차곡차곡 들어간 카운팅 리스트로 바뀜.
    # 그러면 이 count list 에서 하나씩 뽑으면서 최대값 찾아 볼거.

    max_num = 0
    for num in count_list:
        if max_num < num:
            max_num = num

    # 최대값이 찾아졌으면 다시 count_list 에서 하나씩 뽑으면서 그게 최댓값이면 check
    answer_list = []
    for idx, count_num in enumerate(count_list):
        if count_num == max_num:
            answer_list = [idx, count_num]
    m += 1

    print('#{} {} {}'.format(m, answer_list[0], answer_list[1]))
