import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

cnt = [0] * (M+1)
for i in arr:
    cnt[i] += 1
    
ans = 0
for i in range(1, M+1):
    for j in range(i+1, M+1):
        ans += cnt[i] * cnt[j]
print(ans)
