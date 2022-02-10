import sys
sys.stdin = open('input.txt')


def bus(bus_routes):
    bus_stations = [0] * 5000
    answers = []
    for _ in range(bus_routes):
        station_a, station_b = map(int, input().split())
        for ind in range(station_a-1, station_b):
            bus_stations[ind] += 1

    P = int(input())

    for _ in range(P):
        station_c = int(input())
        answers.append(bus_stations[station_c-1])

    return answers


T = int(input())

for tc in range(T):
    routes = int(input())
    answer_list = bus(routes)
    print(f'#{tc + 1}', end=' ')
    print(*answer_list, sep=' ', end='\n')
