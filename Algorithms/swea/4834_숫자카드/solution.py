import sys
sys.stdin = open('input.txt')


def number_card(numbers):
    cnt_lst = [0] * 10
    answer_lst = [0, 0]

    for number in numbers:
        cnt_lst[number] += 1

    max_num = 0
    for ind, cnt in enumerate(cnt_lst):
        if cnt >= max_num:
            max_num = cnt
            answer_lst[0] = ind
            answer_lst[1] = cnt

    return answer_lst


T = int(input())

for tc in range(T):
    n = int(input())
    numbers_list = list(map(int, str(input())))
    answers = number_card(numbers_list)
    print(f'#{tc+1} {answers[0]} {answers[1]}')
