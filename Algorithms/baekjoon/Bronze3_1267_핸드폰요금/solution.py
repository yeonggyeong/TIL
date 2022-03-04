n = int(input())

fares = list(map(int, input().split()))

y_fare = 0
m_fare = 0

for fare in fares:
    while fare // 30 > 0:
        y_fare += 10
        fare = fare - 30
    y_fare += 10

for fare in fares:
    while fare // 60 > 0:
        m_fare += 15
        fare = fare-60
    m_fare += 15

answers = []
if y_fare == m_fare:
    answers.append('Y')
    answers.append('M')
    answers.append(str(m_fare))
elif y_fare > m_fare:
    answers.append('M')
    answers.append(str(m_fare))
else:
    answers.append('Y')
    answers.append(str(y_fare))

print(' '.join(answers))