from collections import deque

def solution(maps):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    answer = bfs(0, 0, maps, n, m, visited)
    if (answer == 1): return -1
    else: return answer

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, maps, n, m, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            xx = nx + dx[i]
            yy = ny + dy[i]
            if (0 <= xx < n and 0 <= yy < m):
                if (not visited[xx][yy] and maps[xx][yy] != 0):
                    visited[xx][yy] = True
                    queue.append((xx, yy))
                    maps[xx][yy] = maps[nx][ny] + 1
    return maps[n-1][m-1]
    
                
    
