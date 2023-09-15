import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
ans = 0
for i in range(N):
    if (i < K and A[i] < B[N-i-1]):
        ans += B[N-i-1]
    else: ans += A[i]
print(ans)
    
