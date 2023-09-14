import sys
from collections import deque
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
INF = 10**9
graph = [INF for _ in range(F)]

graph[S-1] = 0
dx = [U, -D]

def bfs(x):
    queue = deque()
    graph[x] = 0
    queue.append(x)
    while queue:
        v = queue.popleft()
        for i in range(2):
            nx = v + dx[i]
            if (nx >= 0 and nx < F and graph[nx] == INF):
                graph[nx] = graph[v] + 1
                queue.append(nx)
    return graph[G-1]

ans = bfs(S-1)
if (ans == INF): print('use the stairs')
else: print(ans)

