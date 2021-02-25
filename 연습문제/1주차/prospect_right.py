initial_input = int(input())
buildings_list = list(map(int, input().split()))

# 숫자 하나씩 튀어 나올텐데? 일단 그 인덱스 기준으로 왼쪽 1칸, 왼쪽 2칸, 오른쪽 1칸, 오른쪽 2칸 에 위치해있는 빌딩보다 일단 지가 젤 높아야 하고?
# 그럼 5개 빌딩 버블소팅 하고 맨 마지막거랑 맨 마지막에서 두번째의 차가 내가 원하는 갯수. 그거 주워모아서 answer에 더해줌.
answer = 0
for i in range(2, len(buildings_list)-1):
    if  buildings_list[i] > buildings_list[i-1] and buildings_list[i] > buildings_list[i-2] and buildings_list[i] > buildings_list[i+1] and buildings_list[i] > buildings_list[i+2]:
        unsorted_list = [buildings_list[i-2],buildings_list[i-1],buildings_list[i],buildings_list[i+1],buildings_list[i+2]]
        for j in range(4,0,-1):
            for k in range(0,j):
                if unsorted_list[k] > unsorted_list[k+1]:
                    unsorted_list[k],unsorted_list[k+1] = unsorted_list[k+1], unsorted_list[k]
        answer += unsorted_list[-1] - unsorted_list[-2]

print(answer)






