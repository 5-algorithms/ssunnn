# 백준 알고리즘 10773
# 제로

k = int(input())
m = []

for i in range(k):
    num = int(input())
    if num == 0:
        m.pop()
    else:
        m.append(num)

print(sum(m))