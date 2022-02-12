def hanoi(start, median, end, n):

    if n == 1:
        print(start, end, sep = " ")
        return
    hanoi(start, end, median, n-1)
    hanoi(start, median, end, 1)
    hanoi(median, start, end, n-1)


n = int(input())
move = (2 ** n) - 1
print(move)
if n <= 20:
    hanoi(1, 2, 3, n)