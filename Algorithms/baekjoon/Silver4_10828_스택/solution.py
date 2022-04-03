import sys
N = int(sys.stdin.readline())

orders = [list(sys.stdin.readline().split()) for _ in range(N)]

stack = []

for order in orders:
    if order[0] == 'push':
        stack.append(int(order[1]))
    elif order[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)
