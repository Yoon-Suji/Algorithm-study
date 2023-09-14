import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

def dfs(x, y):
    if (x < 0 or x >= N or y < 0 or y >= M): return False
    if (graph[x][y] == 0):
        graph[x][y] = 1 # 방문 처리
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x, y-1)
        return True
    return False

ans = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            ans += 1
print(ans)

