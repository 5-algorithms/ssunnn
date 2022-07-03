#백준 알고리즘 2217번
#로프

n = int(input())
rope=[]
value=[]
for i in range(n):
    rope.append(int(input()))
rope.sort(reverse=True)
for num in range(n):
    value.append(rope[num]*(num+1))
print(max(value))