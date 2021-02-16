T = int(input())

for tc in range(1, T+1):
    P, A, B = list(map(int, input().split()))
    # P = 전체쪽수, A = a 가 찾을 쪽번호, B = b가 찾을 쪽 번호
    book_pages = [x for x in range(1, P+1)]

    def binary_search(target):
        l = 1
        r = P
        try_count = 0
        while l < r:
            c = int((l+r)/2)
            if target > c:  # 내가 찾고자 하는 값이 중점보다 크다면?
                l = c
                try_count += 1

            if target < c:  # 내가 찾고자 하는 값이 중점보다 작으면?
                r = c
                try_count += 1

            if target == c:
                break
        return try_count

    answer = 0

    if binary_search(A) > binary_search(B):
        answer = 'B'

    if binary_search(A) < binary_search(B):
        answer = 'A'

    if binary_search(A) == binary_search(B):
        answer = 0

    print('#{} {}'.format(tc, answer))