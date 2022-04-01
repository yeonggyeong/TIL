from collections import deque

def get_count(N, M):

    queue = deque()
    queue.append([N, 0])

    # 2 + 1 = 3 / 3 -1 = 2 처럼 무한 반복하지 않기 위해 생성
    visited = set()
    visited.add(N)

    while queue:
        n, count = queue.popleft()

        if n == M:
            break
        
        if n + 1 not in visited and n + 1 <= 1000000:
            queue.append((n+1, count+1))
            visited.add(n+1)
        
        if n - 1 not in visited and n - 1 <= 1000000:
            queue.append((n-1, count+1))
            visited.add(n-1)

        if n * 2 not in visited and n * 2 <= 1000000:
            queue.append((n * 2, count+1))
            visited.add(n * 2)

        if n - 10 not in visited and n - 10 <= 1000000:
            queue.append((n - 10, count+1))
            visited.add(n - 10)
    
    return count

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    answer = get_count(N, M)

    print(f'#{tc+1} {answer}')