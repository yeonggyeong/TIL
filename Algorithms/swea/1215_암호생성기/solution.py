def get_password(queue):
    minus = 1
    flag = True
    while flag:
        number = queue.pop(0)
        if number - minus <= 0:
            queue.append(0)
            break 
        queue.append(number-minus)
        minus += 1

        if minus > 5:
            minus = 1

    return queue

for tc in range(10):
    n = int(input())

    queue = list(map(int, input().split()))
    answers = get_password(queue)
    answer = ' '.join(map(str, answers))
    print(f'#{tc+1} {answer}')