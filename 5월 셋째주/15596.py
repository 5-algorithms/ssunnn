# 백준 알고리즘
# 15596번
# 정수 N개의 합
a = list(map(int, input().split()))
def solve(a: list):
    total = 0
    for i in a: 
        total += i
    return total
solve(a)