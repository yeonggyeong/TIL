# 문자열을 찾고 싶은 문자열의 길이만큼 잘라 확인하며, 동일하면 count의 숫자를 1 더해줌
def find_word(string, word):
    count = 0
    for st in range(0, len(string)-len(word)+1):
        if string[st:st+len(word)] == word:
            count += 1
    return count

for tc in range(10):
    num = int(input())
    word = input()
    string = input()
    answer = find_word(string, word)
    print(f'#{num} {answer}')