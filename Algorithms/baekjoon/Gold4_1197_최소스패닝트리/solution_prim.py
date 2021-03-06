# 프림 ->> 732 크루스칼 ->> 4460
import sys, heapq
sys.setrecursionlimit(10 ** 6)

V, E = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]
queue = []
for _ in range(E):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start].append([weight, end])
    graph[end].append([weight, start])

mst = 0
edges = 0
# 처음 시작 가중치, node
queue.append([0, 1])

while queue:
    if edges == V:
        break

    w, n = heapq.heappop(queue)
    if not visited[n]:
        visited[n] = 1
        mst += w
        edges += 1
        for i in graph[n]:
            heapq.heappush(queue, i)

print(mst)