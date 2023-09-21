import sys
input = sys.stdin.readline
INF = 10**9

N, M = map(int, input().split())
dist = [[INF] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    dist[a][b] = 1
    dist[b][a] = 1
X, K = map(int, input().split())


for i in range(1, N+1):
    for j in range(1, N+1):
        if (i == j): dist[i][j] = 0

for i in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            dist[a][b] = min(dist[a][b], dist[a][i] + dist[i][b])
distance = dist[1][K] + dist[K][X]
if (distance > INF): print(-1)
else: print(distance)
