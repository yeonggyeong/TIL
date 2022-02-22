def solution(words):
    stack = []
    for word in words:
        # 여는 괄호이면 stack에 추가
        if word == '(' or word == '{':
            stack.append(word)
        # 닫는 괄호
        elif word == ')' or word == '}':
            # 처음부터 닫는 괄호가 나오면 더 돌지 않고 바로 0 반환
            if not(len(stack)):
                return 0
            
            # 가장 마지막 여는 괄호 반환
            # 가장 마지막 여는 괄호와 현재 닫는 괄호가 짝을 이루지 않는다면 0 반환
            top = stack.pop()
            if word == ')' and top != '(':
                return 0
            elif word == '}' and top != '{':
                return 0
    # 닫는 괄호 없는 여는 괄호가 남아있을 경우에도 0 반환
    if len(stack) > 0:
        return 0

    return 1


T = int(input())

for tc in range(T):
    sentence = list(input())
    answer = solution(sentence)
    print(f'#{tc+1} {answer}')