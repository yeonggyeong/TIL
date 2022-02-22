def get_word(words):
    stack = []
    for i in range(len(words)):
        # 만약 stack이 비어있다면 해당 문자를 추가
        if not(stack):
            stack.append(words[i])
        else:
            # stack이 비어있지않고, 최근 stack에 추가한 값과 현재 문자가 같다면 stack의 마지막 요소 제거
            if stack[-1] == words[i]:
                stack.pop()
            else:
                # 다르다면, 현재 문자 추가
                stack.append(words[i])
    # 남아있는 원소의 개수를 출력
    return len(stack)

T = int(input())
for tc in range(T):
    words = list(input())
    
    answer = get_word(words)
    print(f'#{tc+1} {answer}')