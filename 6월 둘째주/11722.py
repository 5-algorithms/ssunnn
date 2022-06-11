#백준 알고리즘 11722번
#가장 긴 감소하는 부분 수열

#수열 a의 크기 n
n = int(input())
#수열 a를 이루고 있는 ai
a = list(map(int, input().split()))
#감소하는 부분 수열 인덱스 저장하는 배열
dp = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if a[j] > a[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))