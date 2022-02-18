# `in`을 사용하여 함수 생성
# 만약 str1이 str2가 있다면, 1을 반환
# 없다면 0을 반환
def check_string(str1, str2):
    if str1 in str2:
        return 1
    else:
        return 0

T = int(input())

for tc in range(T):

    word = input()
    string = input()
    answer = check_string(word, string)

    print(f'#{tc+1} {answer}')