def dfs(v):

    visited[v] = 1
    for new_v in graph[v][::-1]:
        if not visited[new_v]:
            dfs(new_v)

T = int(input())

for tc in range(1, T+1):
    # V => 정점의 개수, E => 간선의 개수
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]

    # 간선 정보만 들어옴 => 간선의 개수 만큼 입력
    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)

    # 탐색할 시작 Vertex & 종료 Vertex
    S, G = map(int, input().split())
    visited = [0 for _ in range(V+1)]
    dfs(S)
    print(f'#{tc} {visited[G]}')