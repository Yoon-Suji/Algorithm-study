# 정렬
## 선택 정렬
* 매번 가장 작은 것을 선택해서 앞으로 보내는 과정을 반복하는 정렬 방법
* `O(N^2)`의 시간 복잡도를 가진다.
```python
for i in range(len(array)):
  min_index = i
  for j in range(i+1, len(array)):
    if (array[min_index] > array[j]):
      min_index = j
  array[i], array[min_index] = array[min_index], array[i] # 스와프 문법
```

## 삽입 정렬
* 데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입하는 정렬 방법
* 필요할 때만 위치를 바꾸므로 '데이터가 거의 정렬되어 있을 때' 훨씬 효율적이다.
* 특정 데이터가 적절한 위치에 들어가기 전에 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다. 또한 삽입 정렬은 첫 번째 데이터는 그 자체로 정렬되어 있다고 판단하고 두 번쨰 데이터부터 시작한다.
* `O(N^2)`의 시간 복잡도를 가진다.
```python
for i in range(1, len(array)):
  for j in range(i, 0, -1):
    if (array[j] < array[j-1]):
      array[j], array[j-1] = array[j-1], array[j]
    else: # 자기보다 작은 데이터를 만나면 멈춤
      break
```

## 퀵 정렬
* 피벗(pivot)을 기준으로 정렬(분할)을 수행한 이후에, 피벗을 기준으로 나뉜 왼쪽 리스트와 오른쪽 리스트에서 각각 다시 정렬을 수행하는 방법. 제일 많이 사용되는 방법이다.
* 재귀 함수 형태로 동작한다.
* 평균 시간 복잡도는 `O(NlogN)`이지만 최악의 경우 `O(N^2)`의 시간 복잡도를 가진다.
* 삽입 정렬과 반대로 '이미 데이터가 정렬되어 있는 경우'에 매우 느리게 동작한다.
```python
def quick_sort(array, start, end):
  if start >= end: return # 원소가 1개인 경우 종료
  pivot = start # 첫 번째 원소를 피봇으로 설정
  left = start + 1
  right = end
  while left <= right:
    while left <= end and array[left] <= array[pivot]: # 피봇보다 큰 데이터를 찾을 때까지 반복
      left += 1
    while right > start and array[right] >= array[pivot]: # 피봇보다 작은 데이터를 찾을 때까지 반복
      right -= 1
    if left > right: # 엇갈렸다면 작은 데이터와 피봇을 교체
      array[right], array[pivot] = array[pivot], array[right]
    else:
      array[left], array[right] = array[right], array[left]
  quick_sort(array, start, right - 1)
  quick_sort(array, right + 1, end)
```

## 계수 정렬
* '데이터의 크기 범위가 제한되어 있고 정수 형태로 표현할 수 있을 때'만 사용 가능하지만 매우 빠른 정렬 알고리즘
  * 모든 범위를 담을 수 있는 크기의 리스트를 선언해야 하기 때문에 가장 큰 데이터와 가장 작은 데이터의 차이가 너무 클 때는 사용할 수 없다.
  * 데이터의 크기가 많이 중복되어 있을수록 유리하다. 공간 복잡도는 `O(N+K)` 이다.
* 데이터의 개수가 N, 데이터 최댓값이 K일 때 최악의 경우에도 `O(N+K)` 시간 복잡도를 보장한다.
* 데이터 값의 범위가 모두 담길 수 있도록 리스트를 생성하고, 데이터 값과 동일한 인덱스의 리스트를 1씩 증가시킨 후에 리스트의 첫 번째 데이터부터 하나씩 그 값만큼 인덱스를 출력하면 된다.
```python
# 모든 원소의 값이 0 <= value <= 9 라고 가정
count = [0] * (max(array) + 1)

for i in range(len(array)):
  count[array[i]] += 1

for i in range(len(count)):
  for j in range(count[i]):
    print(i)
```

## 파이썬의 정렬 라이브러리
* 파이썬의 기본 정렬 라이브러리인 `sorted()` 함수는 병합 정렬을 기반으로 만들어졌고, 시간 복잡도 `O(NlogN)`을 보장한다.
```python
result = sorted(array) # 정렬된 리스트 반환
array.sort() # 별도의 정렬된 리스트를 반환하지 않고 내부 원소가 정렬됨.
```

### 정렬 알고리즘이 사용되는 문제 유형
1. 정렬 라이브러리로 풀 수 있는 문제
2. 정렬 알고리즘의 원리에 대해 물어보는 문제
3. 더 빠른 정렬이 필요한 문제
