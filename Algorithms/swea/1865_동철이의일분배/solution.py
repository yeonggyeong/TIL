def do_work(start, end, probs):
    global max_prob

    # 선택해야하는 일과 마지막 일이 같다면
    if start == end:
        if probs > max_prob:
            max_prob = probs
        return 
    
    # 마지막 일이 아니더라도 가지치기
    if probs <= max_prob:
        return
    
    for i in range(N):
        # 일이 선택되지 않았다면
        if not works[i]:
            # 현재 확률에 해당 확룔 곱
            now_probs = probs * prob[start][i] * 0.01
            works[i] = 1
            do_work(start+1, end, now_probs)
            works[i] = 0




T  = int(input())

for tc in range(T):
    N = int(input())

    prob = [list(map(int, input().split())) for _ in range(N)]

    # 일의 선택 여부를 담기 위한 리스트
    works = [0 for _ in range(N)]
    max_prob = 0
    do_work(0, N, 1)
    print('#{} {:.6f}'.format(tc+1, max_prob * 100))