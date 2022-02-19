
# 도착하는 방 중 가장 큰방을 기준으로 복도 생성
def get_max_road(roads):
    max_road = 0
    for road in roads:
        if road[0] > max_road:
            max_road = road[0]
        if road[1] > max_road:
            max_road = road[1]

    return max_road

# 복도를 최장길이만큼 생성해서 지나온 길에 +1
# 가장 많은 복도의 값을 반환
# 현재 방 번호보다 돌아가야하는 방 번호가 큰 경우와 작은 경우를 나누기
def get_time(max_road, roads):
    corridors = [0] * max_road

    for road in roads:
        start = (road[0] + 1) // 2
        end = (road[1] + 1) // 2
        if start < end:
            for idx in range(start, end+1):
                corridors[idx] += 1
        else:
            for idx in range(end, start+1):
                corridors[idx] += 1

    corridors = set(corridors)
    time = 0
    for corridor in corridors:
        if corridor > time:
            time = corridor

    return time

T = int(input())

for tc in range(T):
    n = int(input())
    roads = [list(map(int, input().split())) for _ in range(n)]

    max_road = get_max_road(roads)
    answer = get_time(max_road,roads)
    print(f'#{tc+1} {answer}')
