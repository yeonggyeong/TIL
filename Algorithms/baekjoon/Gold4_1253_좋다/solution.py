import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

numbers.sort()

good = 0
for i in range(N):
    new_numbers = numbers[:i] + numbers[i+1:]
    new = numbers[i]
    start, end = 0, len(new_numbers) - 1

    while start < end:
        sum_number = new_numbers[start] + new_numbers[end]
        if sum_number == new:
            good += 1
            break
        elif new > sum_number:
            start += 1
        elif new < sum_number:
            end -= 1
print(good)