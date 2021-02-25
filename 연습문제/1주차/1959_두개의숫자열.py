T = int(input())
t = 0

for tc in range(1,T+1):
    N, M = map(int, input().split())  # N = A 리스트 개수, M = B 리스트 개수
    A = list(map(int, input().split()))  # A 리스트
    B = list(map(int, input().split()))  # B 리스트

    # 전체 큰 포문은 큰수 - 작은수 + 1 번만 돌면 된다.
    # 작은쪽이 큰쪽을 포인팅 인덱스 하나씩 가리켜 가면서.

    if len(A) < len(B):
        collecting_list = []
        for i in range(len(B)-len(A)+1):
            multiplied_sum = 0
            for j in range(len(A)):
                multiplied_sum += A[j] * B[j+i]
            collecting_list.append(multiplied_sum)

        answer = collecting_list[0]

        for each_candidate in collecting_list:
            if answer < each_candidate:
                answer = each_candidate

    if len(A) > len(B):
        collecting_list = []
        for i in range(len(A) - len(B) + 1):
            multiplied_sum = 0
            for j in range(len(B)):
                multiplied_sum += B[j] * A[j + i]
            collecting_list.append(multiplied_sum)

        answer = collecting_list[0]

        for each_candidate in collecting_list:
            if answer < each_candidate:
                answer = each_candidate

    if len(A) == len(B):
        multiplied_list = [x*y for x, y in zip(A, B)]
        answer = 0
        for i in multiplied_list:
            answer += i

    t += 1

    print('#{} {}'.format(t, answer))
