import sys
def change(node):
    p = tree[node][0]

    if p:
        # 부모가 있다면
        if tree[node][3] < tree[p][3]:
            tree[node][3], tree[p][3] = tree[p][3], tree[node][3]
    else:
        # 부모가 없다면
        return
    change(p)


def get_sum(node):
    global answer
    if tree[node][0] == 0:
        return
    else:
        answer += tree[tree[node][0]][3]
        get_sum(tree[node][0])


T = int(input())
for tc in range(T):
    N = int(input())
    inputs = list(map(int, input().split()))
    tree = [[0, 0, 0, 0] for _ in range(N+1)]
    # 이진 트리 생성
    for idx in range(1, N+1):
        tree[idx][3] = inputs[idx-1]
        tree[idx][0] = idx // 2
        if 2 * idx <= N:
            tree[idx][1] = 2 * idx
            tree[idx][2] = 2 * idx + 1
            if 2*idx+1 > N:
                tree[idx][2] = 0

    # 최소 힙을 만들기 위한 과정
    for i in range(1, N + 1):
        change(i)

    answer = 0
    get_sum(N)
    print(f'#{tc+1} {answer}')