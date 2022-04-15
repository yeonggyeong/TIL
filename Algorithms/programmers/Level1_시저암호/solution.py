def solution(s, n):
    strings = list(s)
    new_lst = []

    for string in strings:
        if string == ' ':
            new_lst.append(ord(string))
        else:
            # 무작정 n이 커지게 되면 반복해서 빼줘야 하기 때문에 그 전에 나머지만 더해주기
            new_string = ord(string) + (n % 26)
            # 소문자이고 해당 범위를 넘어가면 / 대문자이고 대문자 범위를 넘어간다면
            if new_string > 122 and string.islower() or string.isupper() and 90 < new_string:
                new_lst.append(new_string - 26)
            else:
                new_lst.append(new_string)
    new_lst = [chr(i) for i in new_lst]
    answer = ''.join(new_lst)
    return answer

s = input()
n = int(input())
print(solution(s, n))