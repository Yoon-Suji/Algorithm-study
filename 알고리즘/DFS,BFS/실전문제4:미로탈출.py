import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))
visited = [[False for _ in range(M)] for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    visited[x][y] = True
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx < 0 or ny < 0 or nx >= N or ny >= M): continue
            if (graph[nx][ny] == 1 and visited[nx][ny] == False):
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[N-1][M-1]

print(bfs(0, 0))
