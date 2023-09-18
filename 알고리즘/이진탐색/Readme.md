# 이진 탐색
## 순차 탐색
* 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 차례대로 하나씩 확인하는 방법
* 파이썬 리스트 자료형의 `count()` 메소드도 내부에서 순차 탐색 사용
* `O(N)` 시간 복잡도
```python
def sequential_search(n, target, array):
  for i in range(n):
    if (array[i] == target):
      return i # 현재 인덱스 반환
```

## 이진 탐색
* 찾으려는 데이터와 중간점에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 과정
* 배열 내부의 데이터가 정렬되어야만 사용할 수 있다.
* `O(logN)` 시간 복잡도
* 처리해야 할 데이터의 개수나 값이 10^8 단위 이상으로 넘어가면 이진탐색과 같이 `O(logN)` 속도를 내는 알고리즘을 활용해야 하는 경우가 많음.
```python
# 재귀함수로 구현
def binary_search(array, target, start, end):
  if (start > end): return None
  mid = (start + end) // 2
  if (array[mid] == target):
    return mid
  elif (array[mid] > target):
    binary_search(array, target, start, mid - 1)
  else:
    binary_search(array, target, mid + 1, end)
```

```python
# 반복문으로 구현
def binary_search(array, target, start, end):
  while (start <= end):
    mid = (start + end) // 2
    if (array[mid] == target):
      return mid
    elif (array[mid] > target):
      end = mid - 1
    else:
      start = mid + 1
  return None
```


## 트리 자료구조
* 큰 데이터를 처리하는 소프트웨어는 대부분 데이터를 트리 자료구조로 저장해서 이진 탐색과 같은 탐색 기법을 이용해 빠르게 탐색이 가능하다.
<img src='https://github.com/Yoon-Suji/Algorithm-study/assets/70956926/4b41c62c-a564-4a73-8202-563f7a60294d' width=500 />
* 트리는 부모 노드와 자식 노드의 관계로 표현된다.
* 트리의 최상단 노드를 루트 노드라고 한다.
* 트리의 최하단 노드를 단말 노드라고 한다.
* 트리에서 일부를 떼어내도 트리 구조이며 이를 서브 트리라고 한다.
* 트리는 파일 시스템과 같이 계층적이고 정렬된 데이터를 다루기에 적합하다.

### 이진 탐색 트리
* 이진 탐색 트리는 **왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드** 가 성립하는 트리이다.
