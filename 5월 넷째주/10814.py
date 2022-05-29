# 백준 알고리즘 10814번
# 나이순 정렬

n = int(input())
list = []

for _ in range(n):
    age, name = map(str, input().split())
    age = int(age)
    list.append((age, name))

list.sort(key = lambda member : (member[0]))

for member in list:
    print(member[0], member[1])