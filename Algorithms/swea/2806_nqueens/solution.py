
def check_queens(r):
    # 대각선, 열 체크
    for i in range(r):
        # 같은 열에 있는 queen이 있거나 대각선에 queen이 있을경우
        if row_idx[r] == row_idx[i] or abs(row_idx[r] - row_idx[i]) == abs(r - i):
            return False
    
    return True
    
def nQueens(r):
    global cnt

    # row가 N이면 성공
    if r == N:
        cnt += 1
        return

    # column 반복
    for i in range(N):
        row_idx[r] = i
        if check_queens(r):
            nQueens(r+1)



T = int(input())

for tc in range(T):
    N = int(input())

    cnt = 0
    # row_idx의 인덱스는 각 row / value는 각 column
    row_idx = [0] * N

    # 0번째 row의 queen
    nQueens(0)
    print(f'#{tc+1} {cnt}')