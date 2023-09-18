# 파라메트릭 서치 유형 (parametric search)
# 원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제에 주로 이용 -> 최적화 문제를 결정 문제(yes or no)로 바꾸어 해결하는 기법
# 현재 이 높이로 자르면 조건을 만족할 수 있는가? -> 대답에 따라 탐색 범위를 좁혀서 해결
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
ans = 0
start = 0
end = arr[-1]

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in arr:
        if i > mid:
            total += i - mid
    if (total < M):
        end = mid - 1
    else:
        start = mid + 1
        ans = mid
print(ans)
