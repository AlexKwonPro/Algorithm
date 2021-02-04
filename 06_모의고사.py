def solution(answers):
    lucky = []

    renouncer_a = 1
    renouncer_b = 2
    renouncer_c = 3

    renouncer_a_answersheet = [1, 2, 3, 4, 5] * 2000
    renouncer_b_answersheet = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    renouncer_c_answersheet = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    
    renouncer_a_correct_count = 0
    renouncer_b_correct_count = 0
    renouncer_c_correct_count = 0

    for random_answer, real_answer in zip(renouncer_a_answersheet, answers):
        if random_answer == real_answer:
            renouncer_a_correct_count += 1

    for random_answer, real_answer in zip(renouncer_b_answersheet, answers):
        if random_answer == real_answer:
            renouncer_b_correct_count += 1
    
    for random_answer, real_answer in zip(renouncer_c_answersheet, answers):
        if random_answer == real_answer:
            renouncer_c_correct_count += 1
    
    answer_count = [renouncer_a_correct_count, renouncer_b_correct_count, renouncer_c_correct_count]

    if max(answer_count) == renouncer_a_correct_count:
        lucky.append(renouncer_a)

    if max(answer_count) == renouncer_b_correct_count:
        lucky.append(renouncer_b)

    if max(answer_count) == renouncer_c_correct_count:
        lucky.append(renouncer_c)
    
    return(sorted(lucky))

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))

# def solution(answers):
#     a = [1,2,3,4,5]
#     b = [2,1,2,3,2,4,2,5]
#     c = [3,3,1,1,2,2,4,4,5,5]

#     score_1=0
#     score_2=0
#     score_3=0

#     for idx, i in enumerate(answers):
#         if answers[idx] == a[idx%5]:
#             score_1 += 1
#         if answers[idx] == b[idx%8]:
#             score_2 += 1
#         if answers[idx] == c[idx%10]:
#             score_3 += 1

#     scores = [score_1, score_2, score_3]
#     result = []
#     for student, score in enumerate(scores,1):
#         if score == max(scores):
#             result.append(student)
#     return result




# def solution(answers):
#     answer = []
#     student1 = [1, 2, 3, 4, 5]
#     student2 = [2, 1, 2, 3, 2, 4, 2, 5]
#     student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
#     student_list = [student1, student2, student3]
#     correct_list = [0, 0, 0]  #1,2,3번 학생의 정답 개수
#     for idx1, s in enumerate(student_list):
#         length = len(s)
#         for idx2, a in enumerate(answers):
#             if a == s[idx2%length]:
#                 correct_list[idx1] += 1
    
#     for idx, i in enumerate(correct_list):
#         if i == max(correct_list):
#             answer.append(idx+1)
            
#     return answer