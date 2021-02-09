T = int(input())
m = 0

for each_tc in range(T):
    track_info = list(map(int, input().split()))
    charging_station_index = list(map(int, input().split()))
    # 일단 충전기가 있는 배열을 만듦. 그 배열의 길이는 0~N

    K = track_info[0]  # 최대이동거리
    N = track_info[1]  # 종점의 길이
    M = track_info[2]  # 충전기가 몇개 설치되었는가?

    # 구간합 구하는것처럼 최대이동거리를 자르고 잘린 오른쪽 끝과
    # 가장 가까이 있는 충전기를 선택해 count 를 1 증가시킴.
    # 만약 구간 자른거안에 충전기가 없으면 0 반환 후 종료
    # 있으면 충전기 다음부터 다시 K 범위로 자름 -> 반복

    # 그냥 메인 배열을 0101화 시킨 charging_station_index 로 하자.
    charging_station_list = [0]*(N+1)
    for i in charging_station_index:
        charging_station_list[i] = 1
    # check_list = [0]*K # 3이 최대이동거리라면 대조할 [0, 0, 0] 리스트만듦. 이방식은 zip 쓸때나 가능할듯.
    count = 0

    start_index = 1
    end_index = 1+K

    while start_index < N - K + 1:
        mini_list = charging_station_list[start_index:end_index]
        for j in range(-1, -1-K, -1):  # 뒤쪽 인덱스 부터 확인하는 절차.
            if mini_list[j] == 1:
                count += 1
                start_index, end_index = end_index + j + 1 , end_index + j + 1 + K
                break  # 하나라도 만나면 브레이크! 이건 while 문을 break 하게됨(?????)
                # 여기서 브레이크 걸리면 for문 종료하는게 맞음. 근데 종료하고나니까 다른게 없어서 와일로 점프뛰는것처럼 보인것!!
        else:
            count = 0  # 그안에 충전소 없으면 0으로 초기화 후 종료.
            break

    m += 1

    print('#{} {}'.format(m, count))




