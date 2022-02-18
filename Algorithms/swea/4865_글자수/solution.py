# str1의 문자열을 key값으로 가지는 dictionary 생성
# str2의 문자열이 str1 dictionary의 키 값 속에 존재한다면, 해당 문자열의 value값의 +1
def make_dictionary(str1, str2):
    count_dic = dict()
    for i in str1:
        count_dic[i] = 0

    for st in str2:
        if st in count_dic.keys():
            count_dic[st] += 1
    
    return count_dic

T = int(input())

for tc in range(T):
    str1 = set(input())
    str2 = input()

    count_dic = make_dictionary(str1, str2)
    # max_value값 찾기
    max_count = 0
    for v in count_dic.values():
        if v > max_count:
            max_count = v

    print(f'#{tc+1} {max_count}')