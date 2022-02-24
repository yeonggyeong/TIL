
def game(v1, v2):
    if v1[1] == v2[1]:
        return v1
    elif (v1[1] == 1 and v2[1] == 3) or (v1[1] == 2 and v2[1] == 1) or (v1[1] == 3 and v2[1] == 2):
        return v1
    else:
        return v2

def get_winner(start, end):

    # 리스트의 길이가 2이하이면 ( 두 카드만 들어있으면 )
    if end - start <= 1:
        return game(cards[start], cards[end])

    # start ~ (start + end) // 2 ->  시작부터 중간지점까지 이긴 사람의 번호와 카드
    first_value = get_winner(start, (start+end)//2)
    # (start + end) // 2 ~ end ->  중간지점부터 끝까지 이긴 사람의 번호와 카드
    second_value = get_winner((start+end)//2 + 1, end)

    return game(first_value, second_value)


T = int(input())

for tc in range(T):
    N = int(input())

    inputs = list(map(int, input().split()))
    cards = []
    for i in range(N):
        cards.append([i, inputs[i]])

    answer = get_winner(0, N-1)
    print(f'#{tc+1} {answer[0] + 1}')