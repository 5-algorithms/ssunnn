# 백준 알고리즘
# 1712번
# 손익분기점
import sys

a, b, c = map(int, sys.stdin.readline().split())

if b>=c:
    print(-1)
else:
    print(int(a/(c-b)+1))