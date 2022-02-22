def get_password(password):
    stack = []
    for i in range(len(password)):
        # 만약 stack이 비어있다면 해당 문자를 추가
        if not(stack):
            stack.append(password[i])
        else:
            # stack이 비어있지않고, 최근 stack에 추가한 값과 현재 문자가 같다면 stack의 마지막 요소 제거
            if stack[-1] == password[i]:
                stack.pop()
            else:
                # 다르다면, 현재 문자 추가
                stack.append(password[i])
    
    return int(''.join(stack))

for tc in range(10):
    n, password = map(str,input().split())
    
    answer = get_password(password)
    print(f'#{tc+1} {answer}')