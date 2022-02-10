import sys
sys.stdin = open('input.txt')


def max_min(lists):
    max_value = min_value = lists[0]
    for number in lists[1:]:
        if number > max_value:
            max_value = number

        if number < min_value:
            min_value = number

    return max_value - min_value


T = int(input())

for tc in range(T):
    n = int(input())
    number_lists = list(map(int, input().split(' ')))
    answer = max_min(number_lists)
    print(f'#{tc+1} {answer}')