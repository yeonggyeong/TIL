import sys
sys.stdin = open('input.txt')

N = int(input())

words = []
# 중복 제거를 위한 임시 리스트
temp = []

for i in range(N):
    word = input()
    # 없는 단어일 경우만 추가
    if word not in temp:
        temp.append(word)
        words.append([word, len(word)])

# 단어 길이로 우선 정렬 및 같다면 사전 순 정렬
words.sort(key=lambda x: (x[1], x[0]))


for word in words:
    print(word[0])