
w, h = map(int, input().split())
k = int(input())
matrix = [[0] * w for _ in range(h)]
# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
idx = 0
# 시작할 위치 설정
x, y = h-1,0

# 만약 자리를 배정할 수 없다면, 0 출력 
if k > w * h:
    print(0)
else:
    # k까지 숫자 채우고, k번째 index 도출
    for i in range(1, k):
        matrix[x][y] = i
        x, y = x+dx[idx], y+dy[idx]
        if not(0 <= x < h) or not(0 <= y < w) or matrix[x][y] != 0:
            x, y = x - dx[idx], y - dy[idx]
            idx = (idx + 1) % 4
            x, y = x+dx[idx], y+dy[idx]
    # 원하는 인덱스 방식으로 맞추기
    print(y+1, h - x)