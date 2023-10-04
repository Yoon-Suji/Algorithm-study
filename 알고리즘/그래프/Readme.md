# 그래프 이론
## 서로소 집합
* **서로소 집합**: 공통 원소가 없는 두 원소. ex) {1, 2}, {3, 4}
* 서로소 집합 자료구조: 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조. `union`, `find` 두 개의 연산으로 조작할 수 있다. `union-find` 자료구조 라고 불리기도 한다.
* `union`: 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
* `find`: 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산
### 서로소 집합 자료구조
* 서로소 집합 자료구조는 **트리 자료구조**를 이용해서 구현한다.
* union 연산을 효과적으로 수행하기 위해 **부모 테이블**을 가지고 있어야 한다. (시작할 때 부모 테이블을 자기 자신으로 초기화해준다.)
> 1. union 연산을 확인해서 서로 연결된 두 노드 A, B를 확인한다.
>  
>    1-1. A와 B의 루트 노드 A', B'를 각각 찾는다.
>    
>    1-2. A'와 B' 중 번호가 더 작은 원소를 부모노드로 가리키도록 설정한다.
> 2. 모든 union 연산을 처리할 때까지 1번 과정을 반복한다.

```python
def find_parent(parent, x):
  # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x:
    return find_parent(parent, parent[x])
  return x

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if (a < b):
    parent[b] = a
  else:
    parent[a] = b
```

하지만 위의 코드는 `find` 함수 실행 시 노드의 개수가 V개 일 때 `O(V)` 의 시간복잡도를 가지므로 비효율적이다.
따라서 **경로 압축** 기법을 적용하여 시간 복잡도를 개선시킬 수 있다.

```python
def find_parent(parent, x):
  if (parent[x] != x):
    parent[x] = find_parent(parent, parent[x])
  return parent[x]
```

위와 같이 코드를 수정하면 각 노드에 대해 find 함수를 호출한 이후에, 해당 노드의 루트 노드가 바로 부모 노드가 되어 루트 노드에 더욱 빠르게 접근할 수 있기 때문에 시간 복잡도가 개선된다.

### 서로소 집합을 활용한 사이클 판별
* 서로소 집합은 무방향 그래프 내에서 사이클을 판별할 때 사용할 수 있다.
> 1. 각 간선을 확인하며 두 노드의 루트 노드를 확인한다.
> 
>    1-1. 루트 노드가 서로 다르다면 두 노드에 대하여 union 연산을 수행한다.
>    
>    1-2. 루트 노드가 서로 같다면 사이클이 발생한 것이다.
> 2. 그래프에 포함되어 있는 모든 간선에 대해 1번 과정을 반복한다.

```python
for i in range(e): # 간선의 개수
  a, b = map(int, input().split()) # 서로 연결된 두 노드 입력받기
  # 사이클 발생 시 종료
  if (find_parent(parent, a) == find_parent(parent, b)):
    cycle = True
    break
  else:
    union_parent(parent, a, b)
```
