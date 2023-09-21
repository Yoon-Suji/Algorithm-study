import sys
import heapq
input = sys.stdin.readline
INF = 10**9

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
X, K = map(int, input().split())

def dijkstra(start, end):
    q = []
    distance = [INF] * (N+1)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if (distance[now] < dist): continue
        for i in graph[now]:
            cost = dist + 1
            if (cost < distance[i]):
                distance[i] = cost
                heapq.heappush(q, (cost, i))
    return distance[end]

k = dijkstra(1, K)
x = dijkstra(K, X)
if (k == INF or x == INF): print(-1)
else: print(k + x)
    
