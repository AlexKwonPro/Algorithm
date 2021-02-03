def solution(array, commands):
    answer = []
    for each_command in commands:
        start_index = each_command[0] - 1
        end_index = each_command[1]
        modified_array = sorted(array[start_index:end_index])
        answer.append(modified_array[each_command[2]-1])

    return answer

print(solution([1,5,2,6,3,7,4], [[2,5,3],[4,4,1],[1,7,3]]))

# array = [1,5,2,6,3,7,4]
# commands = [[2,5,3],[4,4,1],[1,7,3]]
# each_command = [2,5,3]

# start_index = each_command[0] - 1
# end_index = each_command[1]
# modified_array = sorted(array[start_index:end_index])
# print(each_command[2])
# print(modified_array)
# print(modified_array[each_command[2]-1])