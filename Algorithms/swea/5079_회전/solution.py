def solution(rotate, numbers):
    for _ in range(rotate):
        numbers.append(numbers.pop(0))
    
    return numbers[0]

T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))

    rotate = m % n

    answer = solution(rotate, numbers)
    print(f'#{tc+1} {answer}')