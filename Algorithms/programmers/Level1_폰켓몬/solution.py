def solution(nums):

    # 입력 받은 리스트의 중복 제거를 위해 set실행
    distinct = set(list(nums))
    
    # unique한 값이 뽑아야 하는 폰켓몬 보다 많다면
    # 뽑아야 하는 폰켓몬을 다 다르게 선택 가능
    # 아니라면 unique한 값만큼 다른 폰켓몬 선택
    if len(distinct) >= len(nums) // 2:
        answer = len(nums) // 2
    else:
        answer = len(distinct)
    return answer