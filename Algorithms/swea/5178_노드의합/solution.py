# 트리 만들기
def make_tree(N, M):
    tree = [[0, 0, 0, 0] for _ in range(N+1)]

    for idx in range(1, N+1):
        tree[idx][0] = idx // 2
        if 2 * idx <= N:
            tree[idx][1] = 2 * idx
            tree[idx][2] = 2 * idx + 1
            if 2*idx+1 > N:
                tree[idx][2] = 0

    for _ in range(M):
        node, value = map(int, input().split())
        tree[node][3] = value
    return tree

# 후위 순회로 값 채워주기
def post_order(node):
    if node != 0:
        left, right = tree[node][1], tree[node][2]

        post_order(left)
        post_order(right)
        if not tree[node][3]:
            tree[node][3] = tree[tree[node][1]][3] + tree[tree[node][2]][3]


T = int(input())

for tc in range(T):
    N, M, L = map(int, input().split())

    tree = make_tree(N, M)
    post_order(1)
    print(f'#{tc+1} {tree[L][3]}')