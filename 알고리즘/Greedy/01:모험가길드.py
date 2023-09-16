import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort()
ans = 0
cnt = 0
for i in arr:
    cnt += 1
    if (cnt >= i):
        ans += 1
        cnt = 0
print(ans)
    
