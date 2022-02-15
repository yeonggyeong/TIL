# 정렬 함수 생성
def bubble_sort(lst):
    for i in range(len(lst)-1, 0, -1):
        for j in range(0, i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

for tc in range(10):
    dump = int(input())
    box = list(map(int, input().split()))

    # 한번의 상자를 이동할때마다 정렬한후, 가장 높은곳에서 가장 낮은곳으로 상자 이동
    for i in range(dump):
        box = bubble_sort(box)
        box[-1] = box[-1] -1
        box[0] = box[0] + 1

    # dump 횟수만큼 이동한후, 다시 최종 box 들을 정렬하여 최고 높이와 최저 높이 추출
    box = bubble_sort(box)
    max_height = box[-1]
    min_height = box[0]
    diff = max_height - min_height
    print(f'#{tc+1} {diff}')