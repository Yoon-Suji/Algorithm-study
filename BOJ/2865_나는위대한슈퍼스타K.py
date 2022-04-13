import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
ability = [[] for _ in range(N)]
for _ in range(M):
    m = list(map(float, input().split()))
    for i in range(0, N*2, 2):
        ability[int(m[i])-1].append(m[i+1])

for a in ability:
    a.sort(reverse=True)

ability.sort(key=lambda x: -x[0])

ans = 0
for i in range(K):
    ans += ability[i][0]
print(round(ans, 1))
