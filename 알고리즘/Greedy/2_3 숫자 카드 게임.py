# 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수 찾기.
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(sorted(list(map(int, input().split()))))

arr.sort()
print(arr[-1][0])
