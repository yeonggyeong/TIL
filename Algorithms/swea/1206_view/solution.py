def view(number, view_lst):
    view_house = 0

    for num in range(2, number-2):
        height = view_lst[num]
        left_height = view_lst[num-1] if view_lst[num-1] > view_lst[num-2] else view_lst[num-2]
        right_height = view_lst[num+1] if view_lst[num+1] > view_lst[num+2] else view_lst[num+2]

        max_height = left_height if left_height > right_height else right_height
        if height > max_height:
            view_house += height - max_height
        else:
            continue

    return view_house


for i in range(10):
    n = int(input())
    lst = list(map(int, input().split()))
    house = view(n, lst)
    print(f'#{i+1} {house}')
