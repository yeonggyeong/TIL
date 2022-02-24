
def solution(expressions):
    # 숫자가 나올때 마다 담을 stack 생성
    stack = []

    for expression in expressions:
        # 만약 숫자이면 stack에 추가
        if expression.isdigit():
            stack.append(int(expression))
        else:
            # 표현식이 종료될때, stack에 숫자가 한개 있다면 값 반환
            # 표현식이 종료될때, stack에 숫자가 한개가 아니라면 error 반환
            if expression == '.':
                if len(stack) == 1:
                    return stack[-1]
                else:
                    return 'error'
            elif len(stack) < 2:
                return 'error'
            
            # 연산자라면 숫자 두개 뽑기
            number1 = stack.pop()
            number2 = stack.pop()

            if expression == '+':
                stack.append(number1 + number2)
            elif expression == '-':
                stack.append(number2 - number1)
            elif expression == '*':
                stack.append(number1 * number2)
            elif expression == '/':
                stack.append(number2 // number1)


T = int(input())

for tc in range(T):
    expressions = list(input().split())
    
    answer = solution(expressions)
    print(f'#{tc+1} {answer}')