from itertools import combinations

T = int(input())
for tc in range(T):
    numbers = list(range(1, 13))
    n, k = map(int, input().split())
    # combinations를 사용해서 부분집합의 갯수가 n인 부분집합들을 생성
    subset = list(combinations(numbers, n))

    answer = 0
    # 생성된 부분집합을 반복하며 총 합 구하기
    for sub in subset:
        total = 0
        for i in sub:
            total += i
            # 불필요한 연산을 조금이라도 줄이고자 더하는 과정중 k를 넘어가면 실행 중지
            if total > k:
                break
        if total == k:
            answer += 1
    
    print(f'#{tc+1} {answer}')