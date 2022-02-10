import sys
sys.stdin = open('input.txt')


def box_change(boxes, q):
    box_lists = [0] * boxes

    for i in range(1, q+1):
        left, right = map(int, input().split())

        for ind in range(left-1, right):
            box_lists[ind] = i

    return box_lists


T = int(input())

for tc in range(T):
    boxes, q = map(int, input().split())
    answers = box_change(boxes, q)
    print(f'#{tc + 1}', end=' ')
    print(*answers, sep=' ')