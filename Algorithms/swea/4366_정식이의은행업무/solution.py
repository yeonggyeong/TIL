# 이진, 삼진수를 10진수로 변경
def change_number(idx, original, change, num):
    global binary, ternary
    if num == 2:
        binary[idx] = change
        binary_lst.append(int(''.join(binary), 2))
        binary[idx] = original
    else:
        ternary[idx] = change
        ternary_lst.append(int(''.join(ternary), 3))
        ternary[idx] = original

# 한 자리씩 바꿨을 때 나올 수 있는 경우의 수를 모두 생성
def make_lst(binary, ternary):
    global binary_lst, ternary_lst
    for b_idx in range(len(binary)):
        if binary[b_idx] == '0':
            change_number(b_idx, '0', '1', 2)
        else:
            change_number(b_idx, '1', '0', 2)

    for t_idx in range(len(ternary)):
        current = [ternary[t_idx]]

        for i in range(2):
            if ternary[t_idx] == '0':
                if '1' in current:
                    change_number(t_idx, '0', '2', 3)
                else:
                    change_number(t_idx, '0', '1', 3)
                    current.append('1')

            elif ternary[t_idx] == '1':
                if '2' in current:
                    change_number(t_idx, '1', '0', 3)
                else:
                    change_number(t_idx, '1', '2', 3)
                    current.append('2')

            else:
                if '0' in current:
                    change_number(t_idx, '2', '1', 3)
                else:
                    change_number(t_idx, '2', '0', 3)
                    current.append('0')


T = int(input())
for tc in range(T):
    binary = list(input())
    ternary = list(input())
    binary_lst = []
    ternary_lst = []
    make_lst(binary, ternary)

    for binary in binary_lst:
        if binary in ternary_lst:
            answer = binary
            break
    print(f'#{tc+1} {answer}')
