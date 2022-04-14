import sys
input = sys.stdin.readline

N, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

ans = 0
left = 0
right = 0
while (right < N):
    if (arr[right] - arr[left] < L):
        right += 1
    else:
        ans += 1
        left = right
print(ans+1)
