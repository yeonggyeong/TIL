import sys
sys.stdin = open('input.txt')

N = int(input())
customers = [list(input().split()) for _ in range(N)]

# 나이를 int 형으로 변경
customers = [[int(customer[0]), customer[1]] for customer in customers]

# 나이를 기준으로 정렬
customers.sort(key=lambda x: x[0])

for idx in range(N):
    print(customers[idx][0], customers[idx][1])