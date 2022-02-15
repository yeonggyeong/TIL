# 이진탐색의 과정을 count 하는 함수
def binary_search(page, answer_page):
    page_l, page_r = 1, page
    page_c = int((page_l + page_r)/2)

    # page_l, page_r, page_c를 설정했기 때문에 count = 1부터 시작
    search_count = 1
    # 원하는 page와 중간 page가 같을 때까지 반복
    while page_c != answer_page:
        search_count += 1
        # 원하는 page가 더 크다면, page_l과 page_c 수정. page_r은 마지막 페이지로 고정
        if answer_page > page_c:
            page_l = page_c
            page_c = int((page_l + page_r)/2)
        # 원하는 page가 더 작다면, page_r과 page_c 수정. page_l은 첫번째 페이지로 고정
        else:
            page_r = page_c
            page_c = int((page_l + page_r)/2)
    return search_count


T = int(input())
for tc in range(T):
    page, pa, pb = map(int, input().split()) 
    pa_count = binary_search(page, pa)
    pb_count = binary_search(page, pb)
    # count 횟수가 적은 player가 winner 만일, 같다면 0 출력
    if pa_count < pb_count:
        winner = 'A'
    elif pa_count > pb_count:
        winner = 'B'
    else:
        winner = 0

    print(f'#{tc+1} {winner}')