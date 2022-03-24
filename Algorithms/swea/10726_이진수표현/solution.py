T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    # 이진수로 변환
    binary_number = format(M, 'b')

    if len(binary_number) < N:
        answer = 'OFF'

    # 마지막 N개의 글자가 1로만 채워져있다면
    elif binary_number[-N:] == '1'*N:
        answer = 'ON'
    else:
        answer = 'OFF'
    
    print(f'#{tc+1} {answer}')