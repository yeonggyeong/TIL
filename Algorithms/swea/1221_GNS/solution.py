# 행성의 숫자 체계와 우리의 숫자 체계로 dictionary 생성
# 행성의 숫자를 반복하며, value값에 +1
# 정렬을 위해 value가 0이 아니라면 value만큼 반복하여 정렬한 리스트 생성
def solution(numbers):
    num_dict = {'ZRO': 0, 'ONE': 0, 'TWO': 0, 'THR': 0, 'FOR': 0, 'FIV': 0, 'SIX': 0, 'SVN': 0, 'EGT': 0, 'NIN': 0}

    for number in numbers:
        num_dict[number] = num_dict[number]+1

    new_numbers = []
    for k, v in num_dict.items():
        if v != 0:
            for _ in range(v):
                new_numbers.append(k)

    answer = ' '.join(new_numbers)
    return answer

T = int(input())
for tc in range(T):
    num, length = input().split()
    numbers = input().split()
    answer = solution(numbers)
    print(f'{num}')
    print(answer)