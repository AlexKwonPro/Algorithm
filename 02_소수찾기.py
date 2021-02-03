def solution(n):
    answer = 0
    # 소수는 자기자신과 1로만 나누어져야 한다.
    # 어떤수 n 을 인풋받으면 2~n 까지 range 중에

    for i in range(2, n+1): # 이건 소수가 2 이상이라서 그런거.
        if i == 2:
            answer += 1
        else: # 여기가 소수 detecting unit
            for j in range(2, int(i**(1/2))+2):
                if i % j == 0: # 나눠지면 포문 브레이크
                    break
            else:
                answer += 1
# for j in range(2, i): 이렇게 하면 시간초과남 ㅡㅡ
    return answer

# print(solution(10))
# print(solution(5))
# print(solution(20))

# def solution(n):
#     if n == 2:
#         return 1
#     prime_list = [2] # 소수 모음 => return을 위한 값
#     check = [2] # 소수 + sqrt(i)보다 작음 => for문 돌리기 위한 값
#     for i in range(3,n+1):
#         prime = True
#         # 소수 이면서 sqrt(i)보다 작은 숫자만 모은 리스트 check로 for문 돌리기
#         for j in check:
#             if not i % j:
#                 prime = False
#                 break
#         if prime:
#             prime_list.append(i)
        
#         if prime_list[len(check)] <= int((i+1)**(0.5)): # 다음 i를 위한 리스트 check를 준비
#             check.append(prime_list[len(check)]) # 8일 때, check = [2] // 9가 되기 전 check = [2,3]로 만들기
                
            
#     return len(prime_list)