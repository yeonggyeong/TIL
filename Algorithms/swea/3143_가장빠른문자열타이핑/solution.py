def solution(a, b):

    # a의 처음부터 b의 길이만큼 문자열이 b와 같다면, 
    # typing count에 +1
    # i 인덱스를 다음 문자열로 초기화
    i = 0
    typing = 0
    while i < len(a):
        if a[i:i+len(b)] == b:
            i += len(b)
            typing += 1
        else: 
            typing += 1
            i += 1
    
    return typing

T = int(input())

for tc in range(T):
    string, word = input().split()

    answer = solution(string, word)
    print(f'#{tc+1} {answer}')