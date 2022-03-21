def make_tree(N):
    tree = [[0, 0, 0, 0] for _ in range(N+1)]
    for i in range(1, N+1):
        nodes = list(input().split())
        if len(nodes) == 4:
            tree[i][3] = nodes[1]
            tree[i][1] = int(nodes[2])
            tree[i][2] = int(nodes[3])

            tree[int(nodes[2])][0] = i
            tree[int(nodes[3])][0] = i 
        elif len(nodes) == 3:
            tree[i][3] = nodes[1]
            tree[i][1] = int(nodes[2])

            tree[int(nodes[2])][0] = i
        else:
            tree[i][3] = nodes[1]
    return tree

def in_order(node):
    global string

    if node != 0:
        left, right = tree[node][1], tree[node][2]
        in_order(left)
        string += tree[node][3]
        in_order(right)

for tc in range(10):
    N = int(input())
    tree = make_tree(N)
    string = ''
    in_order(1)
    print(f'#{tc+1} {string}')
