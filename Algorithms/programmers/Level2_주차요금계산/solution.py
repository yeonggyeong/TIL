import math

def solution(fees, records):
    
    def calculate_minute(in_time, out_time):
        in_hour, in_minute = map(int, in_time.split(':'))
        out_hour, out_minute = map(int, out_time.split(':'))

        if in_hour == out_hour:
            minute, hour = out_minute - in_minute, 0
        else:
            hour = out_hour - in_hour
            if out_minute < in_minute:
                hour -= 1
                minute = 60 - in_minute + out_minute
            else:
                minute = out_minute - in_minute
        return minute + hour * 60

    def calculate_cost(minutes):
        if minutes <= int(fees[0]):
            return int(fees[1])
        else:
            minutes -= int(fees[0])
            return math.ceil(minutes / int(fees[2])) * int(fees[3]) + int(fees[1])
    
    cars, costs = {}, {}
    for record in records:
        time, number, in_out = record.split()
        # 출차일때
        if in_out == 'OUT':
            costs[number] += calculate_minute(cars[number], time)
            cars.pop(number)
        # 입차일때
        else:
            cars[number] = time
            # 비용 정보 초기화
            if not costs.get(number):
                costs[number] = 0

    for k, v in cars.items():
        costs[k] += calculate_minute(v, '23:59')
        
    costs = sorted(costs.items())
    
    answer = []
    for c in costs:
        answer.append(calculate_cost(c[1]))
        
    return answer