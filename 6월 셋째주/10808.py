#백준 알고리즘 10808번
#알파벳 개수

s = input()
num = [0]*26

for i in range(s):
    num[ord(i)-97]=s.count(i)

for i in num:
    print(i, end=' ')