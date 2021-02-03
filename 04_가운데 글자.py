def solution(s):
    if len(s) % 2:
        return s[int((len(s)/2))]
    else:
        return s[int(len(s)/2-1)] + s[int(len(s)/2)]

# 근데 여긴 왜 int 안붙이면 오류날까?... 4글자 짜리 스트링의 경우.

print(solution('abcde'))
print(solution('qwer'))