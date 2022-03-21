def make_tree(node):
    global number
    if node <= N:
        # 이진 탐색에서 왼쪽 노드의 인덱스는 루트 노드의 두배
        make_tree(node * 2)
        tree[node] = number
        number += 1
        # 이진 탐색에서 오른쪽 노드의 인덱스는 루트 노드의 두배 + 1
        make_tree((node * 2)+1)

T = int(input())

for tc in range(T):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    number = 1
    make_tree(1)

    print(f'#{tc+1} {tree[1]} {tree[N//2]}')