# 백준 알고리즘 1920번
# 수 찾기

n = int(input())
a = sorted(map(int, input().split()))
m = int(input())
b = sorted(map(int, input().split()))

def binary(l, a, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == a[m]:
        return 1
    elif l < a[m]:
        return binary(l, a, start, m-1)
    else:
        return binary(l, a, m+1, end)

for l in b:
    start = 0
    end = len(a)-1
    print(binary(l, a, start, end))