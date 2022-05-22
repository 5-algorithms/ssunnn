# 백준 알고리즘 2606
# 바이러스

com = int(input())
net = int(input())
graph = [[]*com for _ in range(com+1)]

for i in range(net):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [0]*(com+1)
def dfs(start):
    global cnt
    visited[start]=1
    for i in graph[start]:
        if visited[i]==0:
            dfs(i)
            cnt += 1

dfs(1)
print(cnt)