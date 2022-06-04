import sys

R, C = map(int, sys.stdin.readline().split())

strings = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

"""
가장 마지막 줄 부터 확인
확인하면서 중복된 문자 있으면 -1 / 없다면 다음줄 확인
"""
def solution(strings):
    # 중복인지 확인지 확인하기 위해 리스트 생성
    make_str = ['' for _ in range(C)]
    # 최대 값
    answer = R - 1
    flag = False
    while strings:
        string = strings.pop()
        dic = dict()
        # 마지막부터 문자열 더해주기
        for col in range(C):
            make_str[col] += string[col]
            # 겹치는 게 있다면
            if dic.get(make_str[col]):
                flag = True
            else:
                dic[make_str[col]] = 1

        if flag:
            answer -= 1
            flag = False
            if answer == 0:
                return answer
    return answer

print(solution(strings))