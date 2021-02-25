tc_num = int(input())
m = 0

for tc in range(tc_num):

    N, Q = map(int, (input().split()))
    box = [0] * N
    i = 0

    for j in range(Q):
        i += 1
        L, R = map(int, (input().split()))
        for x in range(L, R+1):
            box[x-1] = i

    # print(box)
    answer = ' '.join(map(str, box))
    m += 1

    print("#{} {}".format(m, answer))

# 만약 str(box) 안해주면 join 은 리스트 안의 요소가 str 인 경우 혹은 자체가 스트링인 경우만 받으니까 안된다고 함.
# 그런데 또, 여기서 answer = ' '.join(str(box)) 이렇게하면
# 결과는 -> #1 [ 1 ,   2 ,   2 ,   2 ,   0 ]

