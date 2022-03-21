
# 반복문 밖에 세제곱 리스트 선언
numbers = [i**3 for i in range(10**6+1)]
T = int(input())

for tc in range(T):
    N = int(input())
    answer = -1
    for i in range(len(numbers)):
        if numbers[i] == N:
            answer = i

    print(f'#{tc+1} {answer}')