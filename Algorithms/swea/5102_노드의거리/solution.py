from collections import deque       

def solution(graph):
    S, G =map(int,input().split())
 
    queue = deque()
    queue.append(S)

    visited = [0] * (V + 1)
    visited[S]=1
    while queue:
        n = queue.popleft()
        for i in graph[n]:
            if visited[i]==0:
                queue.append(i)
                visited[i] = visited[n]+1
 
    if visited[G] != 0:
        return visited[G] - 1
    else:
        return 0

T = int(input())    

for tc in range(T):
    V, E = map(int,input().split())
    
    graph = [[]for _ in range(V+1)]

    for _ in range(E):
        x, y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)

    answer = solution(graph)
    print(f'#{tc+1} {answer}')