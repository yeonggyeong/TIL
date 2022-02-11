def hanoi(start, median, end, n):

    if n == 1:
        print(f'{start} {end}')
        return 
    
    hanoi(start, end, median, n-1)
    print(f'{start} {end}')
    hanoi(median, end, start, n-1)


n = int(input())
move = (2 ** n) - 1
print(move)
if n < 20:
    hanoi(1, 2, 3, n)