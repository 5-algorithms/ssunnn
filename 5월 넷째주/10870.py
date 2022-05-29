# 백준 알고리즘 10870번
# 피보나치 수 5
# 동적계획법
# n번째 수가 저장되어 있지 않다면 그 해를 찾아서 저장공간에 넣음으로써 시간 비용을 줄여줌

dp = [0, 1]
def sum(n):
    if n < len(dp):
        return dp[n]
    else:
        total = sum(n-1)+sum(n-2)
        dp.append(total)
        return total
    
n = int(input())
print(sum(n))