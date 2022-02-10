import sys
sys.stdin = open('input.txt')

T = int(input())


def prime_factorization(number):
    prime_list = [2, 3, 5, 7, 11]
    sqared_list = []

    for prime in prime_list:
        sqared = 0
        while not(number % prime):
            number = number // prime
            sqared += 1

        sqared_list.append(sqared)

    return sqared_list


for tc in range(T):
    n = int(input())
    answers = prime_factorization(n)
    print(f'#{tc+1}', end=' ')
    print(*answers, sep=' ')