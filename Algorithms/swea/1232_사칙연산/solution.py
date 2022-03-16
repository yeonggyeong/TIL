def make_tree(n):
            #p l r value
    tree = [[0, 0, 0, 0] for _ in range(n+1)]

    for _ in range(n):
        nodes = list(input().split())
        if len(nodes) == 4:

            tree[int(nodes[0])][1] = int(nodes[2])
            tree[int(nodes[0])][2] = int(nodes[3])
            tree[int(nodes[0])][3] = nodes[1]
            
            tree[int(nodes[2])][0] = int(nodes[0]) 
            tree[int(nodes[3])][0] = int(nodes[0])        
        else:
            tree[int(nodes[0])][3] = int(nodes[1])

    return tree


def post_order(node):
    if node != 0:
        left, right = tree[node][1], tree[node][2]

        post_order(left)
        post_order(right)
        expressions.append(tree[node][3])


def calculator(expressions):
    numbers = []
    for expression in expressions:
        if type(expression) == int:
            numbers.append(expression)
        else:
            number1 = numbers.pop()
            number2 = numbers.pop()
            if expression == '-':
                numbers.append(number2 - number1)
            elif expression == '+':
                numbers.append(number2 + number1)
            elif expression == '*':
                numbers.append(number2 * number1)
            else:
                numbers.append(number2 / number1)
    return int(numbers[-1])


T = 10
for tc in range(T):
    n = int(input())
    # tree 만들기
    tree = make_tree(n)
    expressions = []
    # 후위 순회 사용
    post_order(1)
    # 연산자에 따라 계산기
    answer = calculator(expressions)
    print(f'#{tc+1} {answer}')
