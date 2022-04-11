
def solution(numbers):
    cnt = 0
    for number in numbers:
        # 1은 소수가 아니기 때문에 뛰어넘기
        if number == 1 :
            continue
        
        for i in range(2, number+1):
            # 만약 i로 나누어떨어진다면 멈추기
            if not number % i and i != number:
                break
            elif i == number:
                cnt += 1

    return cnt

n = int(input())
numbers = list(map(int, input().split()))
answer = solution(numbers)
print(answer)