# 버블정렬 이용
def bubble_sort(numbers):
    for i in range(len(numbers)-1, 0, -1):
        for j in range(0, i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

T = int(input())

for tc in range(T):
    n = int(input())
    numbers = list(map(int, input().split()))
    answers = bubble_sort(numbers)
    answers = ' '.join(map(str, answers))
    print(f'#{tc+1} {answers}')