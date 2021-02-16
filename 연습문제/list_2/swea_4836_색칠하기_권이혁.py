T = int(input())

for tc in range(1, T+1):
    area_num = int(input())
    entire_area_list = []

    for _ in range(area_num):
        entire_area_list.append(list(map(int, input().split())))
#######################################################################################
# 좌표들을 전부 뽑아주는 함수

    def slot_coordinate(input_list):
        coordinate_list = []
        r1, c1, r2, c2 = input_list[0], input_list[1], input_list[2], input_list[3]

        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                coordinate_list.append((i,j))

        return coordinate_list

#######################################################################################
    color1_coordinate = []
    color2_coordinate = []

    for each_area in entire_area_list:
        if each_area[4] == 1: # 1번 색이라면
            for each_coordinate_1 in slot_coordinate(each_area):
                color1_coordinate.append(each_coordinate_1)

        if each_area[4] == 2: # 2번 색이라면
            for each_coordinate_2 in slot_coordinate(each_area):
                color2_coordinate.append(each_coordinate_2)

    exclusive_1 = list(set(color1_coordinate))
    exclusive_2 = list(set(color2_coordinate))

    final_exclusive = list(set(exclusive_1 + exclusive_2))

    answer = len(exclusive_1) + len(exclusive_2) - len(final_exclusive)

    print('#{} {}'.format(tc, answer))


