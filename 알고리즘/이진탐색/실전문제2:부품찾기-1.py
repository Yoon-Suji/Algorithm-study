# set 자료형을 사용해 풀면 더 빠르고 간결하게 풀 수 있음.
# 파이썬의 set 자료구조는 해시 테이블을 사용하기 때문에 O(1)의 시간복잡도로 탐색 가능
import sys
input = sys.stdin.readline
N = int(input())
arr = set(map(int, input().split()))
M = int(input())
request = list(map(int, input().split()))

for i in request:
  if i in arr:
    print('yes', end=' ')
  else:
    print('no', end=' ')
