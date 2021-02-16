T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 정수의 갯수 N
    random_numbers = list(map(int, input().split()))

    for i in range(0, len(random_numbers)-1):
        idx = i

        if i % 2:
            for j in range(i+1, len(random_numbers)):
                if random_numbers[j] < random_numbers[idx]:
                    idx = j
            random_numbers[idx], random_numbers[i] = random_numbers[i], random_numbers[idx]

        else:
            for j in range(i+1,len(random_numbers)):
                if random_numbers[j] > random_numbers[idx]:
                    idx = j
            random_numbers[idx], random_numbers[i] = random_numbers[i], random_numbers[idx]

    answer = ' '.join(map(str, random_numbers[:10]))

    print('#{} {}'.format(tc, answer))

