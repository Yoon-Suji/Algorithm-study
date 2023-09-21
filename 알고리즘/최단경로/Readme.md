# 최단 경로
* 가장 짧은 경로를 찾는 알고리즘 문제
* 그리디 알고리즘 및 다이나믹 프로그래밍 알고리즘의 한 유형으로 볼 수도 있다.

## 다익스트라 최단 경로 알고리즘
* 특정한 노드에서 출발해서 다른 모든 노드로 가는 최단 경로를 구해주는 알고리즘
* 음의 간선이 없을 때 정상적으로 동작한다. - 실제로 GPS 소프트웨어의 기본 알고리즘으로 채택되곤 한다.
* 그리디 알고리즘의 한 종류
### 원리
1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 초기화한다.
3. 방문하지 않은 노드 중에서 최단 거리가 제일 짧은 노드를 선택한다.
4. 해당 노드를 거쳐 다른 노드로 가능 비용을 계산하여 최단 거리 테이블을 갱신한다.
5. 위 3, 4번을 반복한다.

### 방법 1. 간단한 다익스트라 알고리즘
* `O(V^2)`의 시간복잡도 (V = 노드의 개수)
* 단계마다 방문하지 않은 노드 중에서 최단 거리가 제일 짧은 노드를 선택하기 위해 매 단계마다 1차원 리스트의 모든 원소를 확인(순차탐색) 한다.

### 방법 2. 개선된 다익스트라 알고리즘
* `O(ElogV)` 의 시간복잡도 (V = 노드의 개수, E = 간선의 개수)
* 힙(Heap) 자료구조를 사용해서 출발 노드로부터 가장 거리가 짧은 노드를 더욱 빠르게 찾을 수 있다.

#### 힙(Heap)
* 우선순위 큐를 구현하기 위해 사용하는 자료구조 중 하나, 우선순위 큐는 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
* 파이썬은 `heapq` 라이브러리를 지원 - 최소 힙 구조
* 하나의 데이터 삽입, 삭제에 `O(logN)` 시간이 소요됨.
```python
import heapq
distance = [INF] * (N+1)

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
```

## 플로이드 와샬 알고리즘
* 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우에 사용할 수 있는 알고리즘
* 다이나믹 프로그래밍
`Dab = min(Dab, Dak + Dbk)` : A에서 B로 가는 최소 비용과 A에서 K를 거쳐서 B로 가는 비용을 비교하여 더 작은 값 갱신
* `O(N^3)` 시간 복잡도
```python
graph = [[INF] * (N+1) for _ in range(N+1)]
for a in range(1, N+1):
  for b in range(1, N+1):
    if (a == b):
      graph[a][b] = 0 # 자기 자신에서 자기 자신으로 가는 비용 0으로 초기화

for _ in range(M):
  a, b, c = map(int, input().split())
  # 간선 정보를 받아서 초기화
  graph[a][b] = c

# 플로이드 와샬 알고리즘 수행
for k in range(1, N+1):
  for a in range(1, N+1):
    for b in range(1, N+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
```
