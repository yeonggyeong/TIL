
def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])

# y가 속한 그룹의 대표자를 x가 속한 그룹의 대표자로 변경
def union(x, y):
    parent[find_set(y)] = find_set(x)


T = int(input())

for tc in range(T):
    # N -> 출석번호 , M -> 신청서
    N, M = map(int, input().split())
    requests = list(map(int, input().split()))

    parent = [i for i in range(N+1)]

    # 한 쌍의 신청서 반복하면서, 두 그룹 병합
    for i in range(0, len(requests), 2):
        union(requests[i], requests[i+1])


    group = []
    # 그룹의 대표자 카운트
    for i in range(N + 1):
        group.append(find_set(i))

    answer = len(set(group)) - 1
    print(f'#{tc+1} {answer}')