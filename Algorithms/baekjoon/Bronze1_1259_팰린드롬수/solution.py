
def solution(number):
    if number == number[::-1]:
        return 'yes'
    else:
        return 'no'

while True:
    number = input()
    if int(number) == 0:
        break

    answer = solution(number)
    print(answer)