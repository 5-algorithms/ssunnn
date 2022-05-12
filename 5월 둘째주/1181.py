# 백준 알고리즘
# 1181번 단어 정렬
import sys

n = int(input())
words = []

for i in range(n):
    words.append(sys.stdin.readline().strip()) # input은 속도가 느림. 따라서 다음과 같이 사용

set_words=set(words)
words=list(set_words)
words.sort() # 괄호 안에 아무 값도 안 넣으면 알파벳 순서대로 정렬해 줌
words.sort(key=len) # 문자열 길이 순으로 정렬

for i in words:
    print(i)