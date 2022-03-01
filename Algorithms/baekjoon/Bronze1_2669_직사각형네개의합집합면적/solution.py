def get_area(positions):
    matrix = [[0] * 100 for _ in range(100)]
    area = 0
    # 직사각형 그리기
    # 겹치는 부분은 넘어가고 겹치지 않는 부분만 채운 후, 면적 +1
    for position in positions:
        for row in range(position[0], position[2]):
            for col in range(position[1], position[3]):
                if matrix[row][col] != 1:
                    matrix[row][col] = 1
                    area += 1

    return area

positions = [list(map(int, input().split())) for _ in range(4)]
answer = get_area(positions)
print(answer)