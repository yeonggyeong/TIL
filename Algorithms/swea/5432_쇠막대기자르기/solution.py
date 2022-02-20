
# ( 다음 바로 ) 가 나오면 레이저로 현재 막대기 만큼 잘린 막대기 추가
# ( 만 나오면 막대기 개수 증가
# ) 만 나오면 막대기 개수 감소 및 잘린 막대기 +1 
def get_stick(problem):
    stick = 0
    cut_stick = 0

    i = 0
    while i < len(problem):
        if problem[i] == '(' and problem[i+1] == ')':
            cut_stick += stick
            i += 2
        elif problem[i] == '(':
            stick += 1
            i += 1
        else:
            cut_stick += 1
            stick -= 1
            i += 1

    return cut_stick

T = int(input())

for tc in range(T):
    problem = input()
    answer = get_stick(problem)

    print(f'#{tc+1} {answer}')