def make_tree(E):
    tree = [[0, 0, 0] for _ in range(E+2)]
    line = list(map(int, input().split()))

    for idx in range(0, E * 2, 2):
        p, c = line[idx], line[idx+1]
        if tree[p][1]:
            tree[p][2] = c
        else:
            tree[p][1] = c
        tree[c][0] = p
    return tree

# 중위 순회시 print 대신 subtree의 개수를 count 
def in_order(node):
    global subtree
    if node != 0:
        left, right = tree[node][1], tree[node][2]

        in_order(left)
        subtree += 1
        in_order(right)

T = int(input())
for tc in range(T):
    E, N = map(int, input().split())
    tree = make_tree(E)
    subtree = 0 
    in_order(N)
    print(f'#{tc+1} {subtree}')