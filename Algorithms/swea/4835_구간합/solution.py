import sys
sys.stdin = open('input.txt')


def sum_diff(number, section_length, number_lst):
    max_sum = 0
    min_sum = 9999999999999999999999

    for ind in range(n-section_length+1):
        section_sum = 0
        for i in range(section_length):
            section_sum += number_lst[ind+i]

        if section_sum >= max_sum:
            max_sum = section_sum
        if section_sum <= min_sum:
            min_sum = section_sum

    return max_sum - min_sum


T = int(input())
for tc in range(T):
    n, m = map(int, input().split(' '))
    numbers = list(map(int, input().split(' ')))
    answer = sum_diff(n, m, numbers)
    print(f'#{tc+1} {answer}')