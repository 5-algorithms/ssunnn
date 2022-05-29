# 백준 알고리즘 3034번
# 앵그리 창영

n, w, h = map(int, input().split())
for i in range(n):
    a = int(input())
    if a <= (w**2+h**2)**0.5 :
        print("DA")
    else:
        print("NE")