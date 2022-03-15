
def get_last_pizza(cheese):
    oven = []
    remain_pizza = []
    # 화덕에 있는 피자, 남아있는 피자 분류
    for idx, ch in enumerate(cheese):
        if idx < n:
            oven.append([idx+1, ch])
        else:
            remain_pizza.append([idx+1, ch])

    # 화덕에 있는 피자의 수가 1개이면 종려
    while len(oven) > 1:
        # 처음에 넣은 피자의 치즈를 줄여주기
        current_pizza = oven.pop(0)
        current_pizza[1] = current_pizza[1] // 2

        # 치즈가 0이고 남아있는 피자가 있다면 화덕에 넣기
        if current_pizza[1] == 0:
            if remain_pizza:
                oven.append(remain_pizza.pop(0))
        else:
            # 녹일 치즈가 남아있다면 다시 화덕에 넣기
            oven.append(current_pizza)

    return oven[0][0]


T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    cheese = list(map(int, input().split()))
    answer = get_last_pizza(cheese)
    print(f'#{tc+1} {answer}')