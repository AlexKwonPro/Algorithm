# 괄호검사
# 1. 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 한다 =
# == 다끝났는데 스택에 남아있으면 안됨.
# 2. 같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야 함.
# == 애초에 오른쪽부터 시작하면 안된다는 뜻임 (스택이 0 인 상태에서 오른쪽 괄호가 뽑히면 안됨)
# 3. 괄호 사이에는 포함 관계만 존재한다.
# == 오른쪽애들 만나면 스택에서 마지막으로 쌓인 왼쪽애 팝해서 대조해 봐야함.

T  = int(input())

for tc in range(1, T+1):
    test_case = input()  # 근데 테스트케이스가 지저분하게 괄호가 아닌것부터 시작할수도 있잖아?
    # 혹은 아예 괄호가 테스트케이스 내에 존재 하지도 않는 경우 괄호 검사 자체는 TRUE 로 떠야함.
    stack = []
    left_bracket = ['{', '(']
    right_bracket_curly = '}'
    right_parenthesis = ')'

    for each_string in test_case:
        if each_string in left_bracket:  # 여기 is '{' or '(' 이런식으로 해도 될듯.
            stack.append(each_string)  # 일단 왼쪽애들이 나오면 열심히 넣어준다.

        if each_string == right_bracket_curly or each_string == right_parenthesis:
            # 만약 해당 위치가 오른쪽 괄호라면, 일단 스택이 비어 있지 않은지를 봐야함. (2번 조건)
            # stack에서 가장 늦게 들어간 왼쪽애 하나를 팝하고 비교 (3번조건)
            if stack == []:
                print('#{} {}'.format(tc, 0))
                break
            else:
                varification = stack.pop()
                if each_string == right_bracket_curly and varification != left_bracket[0]: # 같지 않으면
                    print('#{} {}'.format(tc, 0))
                    break
                if each_string == right_parenthesis and varification != left_bracket[1]:
                    print('#{} {}'.format(tc, 0))
                    break

    else: # 위에 무사히 브레이크 안걸리고 돌았으면 괜찮은거임.
        if stack != []:  # 검사가 다 끝났는데 스택이 비지 않았다? 짝이 안맞는거임. 1번 조건에 위배.
            print('#{} {}'.format(tc, 0))
        else:
            print('#{} {}'.format(tc, 1))


