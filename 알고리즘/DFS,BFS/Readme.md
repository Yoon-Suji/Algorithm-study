# DFS / BFS
## 탐색
* 탐색: 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
### 스택 (Stack)
* First In Last Out 구조
* Python에서는 기본 리스트에서 `append()` 와 `pop()` 메서드를 사용해서 구현할 수 있다.
### 큐 (Queue)
* First In First Out 구조
* Python에서는 `collections` 모듈에서 사용하는 `deque` 자료구조를 활용하면 속도가 빠르다.
```python
from collections import deque
queue = deque()
queue.append(2) # 삽입
queue.popleft() # 삭제
queue.reverse() # 순서를 역순으로 바꾸기
```
### 재귀함수 (Recursive Function)
* 자기 자신을 다시 호출하는 함수
* 무한 호출을 막기 위해서는 종료 조건을 꼭 명시해야 함
* 컴퓨터 내부에서 재귀 함수의 수행은 스택 자료구조를 이용하므로 스택 자료구조를 활용하는 상당수 알고리즘은 재귀 함수를 이용해서 간편하게 구현할 수 있다. ex) DFS

#### 팩토리얼 예제
팩토리얼을 점화식으로 표현하면 다음과 같다.
* 0 < n <= 1 : `factorial(n) = 1`
* n > 1 : `factorial(n) = n * factorial(n-1)`
```python
def factorial_recursive(n):
  if (n <= 1):
    return 1
  return n * factorial_recursive(n-1)
```
재귀 함수는 반복문을 이용할 때보다 더욱 간결한 형태로 코드를 작성할 수 있다.

## 그래프
<img src="https://github.com/Yoon-Suji/Algorithm-study/assets/70956926/16845f5b-e3b2-4342-99c9-210dece15207"  height="300"/>

### 그래프 표현 방법
* **인접 행렬 (Adjacency Matrix)** : 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식
  * 메모리 측면에서 보면 인접 행렬 방식은 모든 관계를 저장하므로 노드 개수가 많을 수록 메모리가 불필요하게 낭비되지만 특정한 두 노드가 연결되어 있는지 정보를 빠르게 얻을 수 있다.
```python
INF = 999999999 # 연결 되어 있지 않은 노드를 위한 무한의 비용 선언
graph = [
  [0, 7, 5],
  [7, 0, INF],
  [6, INF, 0]
]
```
* **인접 리스트 (Adjacency List)** : 연결 리스트로 그래프의 연결 관계를 표현하는 방식
  * 특정한 노드와 연결된 모든 인접 노드를 순회해야 하는 경우 인접 리스트 방식이 메모리 공간의 낭비가 더 적다.
```python
graph = [[] for _ in range(3)]

graph[0].append((1, 7))
graph[0].append((2, 5))
graph[1].append((0, 7))
graph[2].append(0, 5))
```

## DFS: 깊이 우선 탐색
* 데이터 개수가 N개인 경우 `O(N)` 의 시간이 소요된다.
* 실제 구현 과정은 재귀 함수를 이용했을 때 간결하게 구현할 수 있다.
### 동작 과정
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

### 구현
```python
def dfs(graph, v, visited):
  visited[v] = True # 방문 처리 visited = [False] * N
  print(v)
  for i in graph[v]: # 인접 리스트로 구현한 경우
    if not visited[i]:
      dfs(graph, i, visited)
```

## BFS: 넓이 우선 탐색
* 데이터 개수가 N개인 경우 `O(N)` 의 시간이 소요되지만 일반적인 경우 실제 수행 시간은 DFS보다 좋은 편이다.
* 실제로 구현할 때는 deque 라이브러리를 사용하는 것이 좋다.
### 동작 과정
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

### 구현
```python
from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True # 방문 처리
  while (queue):
    v = queue.popleft()
    print(v)
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
```
