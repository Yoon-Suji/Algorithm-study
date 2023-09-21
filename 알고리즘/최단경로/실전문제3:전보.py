import sys
import heapq
input = sys.stdin.readline
INF = 10**9

N, M, C = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x].append([y, z])

distance = [INF] * (N+1)

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if (dist > distance[now]): continue
        for v, d in graph[now]:
            cost = dist + d
            if (cost < distance[v]):
                distance[v] = cost
                heapq.heappush(q, (cost, v))
dijkstra(C)
cnt = 0
time = 0
for i in range(1, N+1):
    if (distance[i] == INF): continue
    cnt += 1
    time = max(time, distance[i])
    
print(cnt - 1, time)
