# 백준 알고리즘 2884번
# 알람 시계

h, m = map(int, input().split())

if m>=45:
    print(h, m-45)
elif m<45 and h>0:
    print(h-1, m+15)
else:
    print(23, m+15)