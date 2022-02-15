T = int(input())

# 버블 정렬하기 -> 인정합 숫자 비교
def bubble_sort(numbers):
    for i in range(len(numbers)-1, 0, -1):
        for j in range(0, i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


for tc in range(T):
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers = bubble_sort(numbers)
    # 새로운 결과값을 담을 리스트
    results = []
    # 10개의 숫자만을 추출하기 때문에 range(5)로 설정
    # 오름차순으로 정렬되어있는 numbers의 마지막요소(최댓값), 첫번째요소(최솟값) 출력
    for idx in range(5):
        results.append(numbers[len(numbers)-idx-1])
        results.append(numbers[idx])

    results = ' '.join(map(str, results))
    print(f'#{tc+1} {results}')