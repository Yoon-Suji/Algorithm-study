import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()

ans = 0
for i in range(N):
    ans = max(ans, arr[i]*(N-i))
print(ans)
    
    
