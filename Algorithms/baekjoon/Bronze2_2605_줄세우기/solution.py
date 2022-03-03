# 학생 수 
n = int(input())
# 학생이 뽑은 번호의 수
numbers = list(map(int, input().split()))

# 학생 초기 정렬
students = [i for i in range(1, n+1)]

# 움직일 학생을 추출한 후, 뽑은 번호만큼 현재 위치에서 앞에 배치
for idx, number in enumerate(numbers):
    move = students.pop(idx)
    students.insert(idx-number, move)

answers = ' '.join(map(str, students))
print(answers)