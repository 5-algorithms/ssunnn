# 백준 알고리즘 1912번
# 연속합

n = int(input())
perm = list(map(int, input().split()))
total = [0]*n
total[0] = perm[0]

for i in range(1, n):
    total[i] = max(perm[i], total[i-1]+perm[i])


print(max(total))