
x, y, w, h = map(int, input().split())

distances = []

# 현재 x좌표와 y좌표 반복
for i in [x, y]:
    # x 일때 현재 좌표가 넓이의 반을 기준으로 조건 분기
    if i == x:
        if i > (w / 2):
            distances.append(w - i)
        else:
            distances.append(i - 0)
    # y 일때 현재 좌표가 높이의 반을 기준으로 조건 분기
    else:
        if i > (h / 2):
            distances.append(h - i)
        else:
            distances.append(i - 0)

print(min(distances))