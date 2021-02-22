T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split())) # N은 행열 수, M = 타깃의 글자길이
    word_map = [list(input().split()) for _ in range(N)]

    def palindrome_detector(string): # 일단 디텍팅 유닛 뽑고
        check = ''
        for i in string:
            check = i + check

        if check == string:
            return True
        else:
            return False

    # 세로로 확인하지말고 인덱스 슬라이싱 할거면 다 가로로 만들어 버리자. -> 전치행렬 쓰면됨.
    # 문제는 첫번째 인덱스가 ['GOFFAKWFSM'] 이렇게 돼있다는건데, 이걸 아래처럼
    # ['G', 'O', 'F', 'F', 'A', 'K', 'W', 'F', 'S', 'M']
    # 이렇게 만들어서 전치시키고 다시 붙이면 완성!

    def transpose(input_list): # 전치행렬 생성기 + 쪼갰던거 스트링으로 붙이는거까지 해주자
        pendency_list = []  # 일단 찢긴 버전으로 만들고
        for each_list in input_list:
            pendency_list.append(list(each_list[0]))  # --> 그럼 일단 행렬 됨 + 그다음 전치

        for a in range(N):  # 요기까지 하면 pendency list는 전치되었을것.
            for b in range(N):
                if a < b:
                    pendency_list[a][b], pendency_list[b][a] = pendency_list[b][a], pendency_list[a][b]

        final_list = []
        for c in pendency_list: # 찢긴거 다시 붙여
             final_list.append([''.join(c)])

        return final_list

    answer = 0

    for each_horizontal_line in word_map:  # 하나씩 뽑을건데
        for j in range(N-M+1):
            if palindrome_detector(each_horizontal_line[0][j:j+M]):
                answer = each_horizontal_line[0][j:j+M]

    for each_vertical_line in transpose(word_map): # 전치쪽에서 세로애들 나올수도 있음.
        for k in range(N - M + 1):
            if palindrome_detector(each_vertical_line[0][k:k+M]):
                answer = each_vertical_line[0][k:k+M]

    print('#{} {}'.format(tc, answer))







