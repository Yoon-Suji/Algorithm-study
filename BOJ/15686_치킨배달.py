import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
chicken = []
homes = []

for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        if (arr[j] == 2):
            chicken.append([i, j])
        elif (arr[j] == 1):
            homes.append([i, j])

comb = list(combinations(chicken, M))
ans = 1000000
for c in comb:
    result = 0
    for i, j in homes:
        dist = 2500
        for k in range(M):
            tmp = abs(i-c[k][0]) + abs(j-c[k][1])
            dist = min(tmp, dist)
        result += dist
    ans = min(ans, result)
print(ans)
