import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
visit = [False] * (N+1)
ans = [-1] * (N+1)
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)

def bfs(start):
    queue = deque()
    queue.append(start)
    visit[start] = True
    ans[start] = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if (visit[i] == False):
                visit[i] = True
                ans[i] = ans[v] + 1
                queue.append(i)
    return ans

ans = bfs(X)
flag = False
for i in range(len(ans)):
    if (ans[i] == K): 
        flag = True
        print(i)
if (flag == False): print(-1) 
