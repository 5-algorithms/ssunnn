#백준 알고리즘 2178번 - 지정문제
#미로 탐색
from collections import deque

#행, 열 입력
n, m = map(int, input().split())
#미로 2차원 배열
graph = []

#미로 배열 input
for i in range(n):
    graph.append(list(map(int, input().split())))

#이동 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y =  queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue

            if graph[nx][ny]==0:
                continue

            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx, ny))

    return graph[n-1][m-1]

print(bfs(0, 0))