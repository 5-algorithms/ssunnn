#백준 알고리즘 2667번
#단지번호붙이기
from collections import deque

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    n = len(graph)
    queue = deque()
    queue.append((x, y))
    graph[x][y]=0
    cnt=1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=0:
                continue

            if graph[nx][ny]==1:
                graph[nx][ny]=0
                queue.append((nx, ny))
                cnt+=1
    return cnt

cnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])