# def solution(participant, completion):
#     for finisher in completion:
#         participant.remove(finisher)
#     return participant[0]
# # 시간초과 크리티컬...

# def solution(participant, completion):
#     while completion != []:
#         finisher = completion.pop()
#         participant.remove(finisher)

#     return participant[0]
# # 무슨 이놈도 시간초과.. pop 으로 iterable 숫자 줄였는데도..

def solution(participant, completion):
    sorted_participant = sorted(participant)
    sorted_completion = sorted(completion)
    
    for contender, finisher in zip(sorted_participant, sorted_completion):
        if contender != finisher:
            return contender
    else:
        return sorted_participant[-1]


participant=['leo', 'kiki', 'eden']
completion = ['eden', 'kiki']

print(solution(['leo', 'kiki', 'eden'],['eden', 'kiki']))