tc_num = int(input())
m = 0
prime_number_list = [2, 3, 5, 7, 11]

for tc in range(tc_num):
    composite_number = int(input())
    divisor_list = []

    for prime in prime_number_list:
        cnt = 0
        while composite_number % prime == 0:
            composite_number //= prime
            cnt += 1
        divisor_list.append(cnt)

    answer = ' '.join(map(str, divisor_list))
    m += 1

    print("#{} {}".format(m, answer))